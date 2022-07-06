import asyncio
import json
import pika


class Producer():
    def __init__(self, connections):
        self.connections = connections

        self.rmq_connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel = self.rmq_connection.channel()
        self.queue = "Producer"


    def handler(self):
        self.channel.basic_consume(queue=self.queue,
                                   auto_ack=True,
                                   on_message_callback=self.callback)
        self.channel.start_consuming()

    def callback(self, ch, method, properties, body):
        i_data = json.loads(body)
        recipients = i_data["recipients"]
        del i_data["recipients"]
        for r in recipients:
            asyncio.run(self.connections[r].send(json.dumps(i_data)))


