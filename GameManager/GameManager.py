import asyncio
import json
import threading

from Match import Match
from Utils.RabbitMQ import RabbitMQ


class GameManager:
    def __init__(self):
        self.consumer = RabbitMQ("GameManager")
        self.producer = RabbitMQ("Producer")
        self.actions = self._init_actions()
        self.queue = []
        self.matches = {}

    def callback(self, ch, method, properties, body):
        i_body = json.loads(body)
        self.actions[i_body["action"]](i_body["sender"])

    def run(self):
        threading.Thread(target=self.processor).start()
        self.consumer.consuming(self.callback)

    def _init_actions(self):
        return {
            "join_queue": self.join_queue,
            "quit_queue": self.quit_queue,
        }

    def join_queue(self, conn):
        self.queue.append(conn)
        o_data = {
            "action": "join_queue",
            "recipients": [conn],
            "status": "accept",
        }
        self.producer.send(json.dumps(o_data))

    def quit_queue(self, conn):
        self.queue.remove(conn)
        o_data = {
            "action": "quit_queue",
            "recipients": [conn],
            "status": "accept",
        }
        self.producer.send(json.dumps(o_data))

    def processor(self):
        while True:
            if len(self.queue) > 0 and len(self.queue) % 2 == 0:
                p1 = self.queue.pop()
                p2 = self.queue.pop()
                print(type(p1), type(p2))
                match = Match(p1, p2)
                self.matches[match.id] = match
                o_data = {
                    "action": "match_created",
                    "recipients": [p1, p2],
                    "attrs": {
                        "id": match.id
                    }
                }
                self.producer.send(json.dumps(o_data))


