import json

from Utils.RabbitMQ import RabbitMQ


class MatchMaking:
    def __init__(self):
        self.consumer = RabbitMQ("MatchMaking")
        self.producer = RabbitMQ("Producer")
        self.actions = self._init_actions()
        self.queue = []

    def callback(self, ch, method, properties, body):
        i_body = json.loads(body)
        self.actions[i_body["action"]](i_body["sender"])

    def run(self):
        self.consumer.consuming(self.callback)

    def _init_actions(self):
        return {
            "join_queue": self.join_queue,
            "quit_queue": self.quit_queue,
        }

    def join_queue(self, conn):
        self.queue.append(conn)
        o_data = {
            "recipients": [conn],
            "action": "join_queue",
            "status": "accept",
        }
        self.producer.send(json.dumps(o_data))

    def quit_queue(self, conn):
        self.queue.remove(conn)
        o_data = {
            "recipients": [conn],
            "action": "quit_queue",
            "status": "accept",
        }
        self.producer.send(json.dumps(o_data))
