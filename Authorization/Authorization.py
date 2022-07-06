import json

from Utils.RabbitMQ import RabbitMQ

class Authorization:
    def __init__(self):
        self.consumer = RabbitMQ("Authorization")
        self.producer = RabbitMQ("Producer")
        self.actions = self._init_actions()

    def callback(self, ch, method, properties, body):
        i_body = json.loads(body)
        self.actions[i_body["action"]](i_body["sender"])

    def run(self):
        self.consumer.consuming(self.callback)

    def _init_actions(self):
        return {
            "sign_in": self.sign_in,
            "sign_up": self.sign_up,
        }

    def sign_in(self, sender, data):
        pass

    def sign_up(self, sender, data):
        pass