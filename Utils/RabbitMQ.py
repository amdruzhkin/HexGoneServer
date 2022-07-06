import pika

class RabbitMQ:
    def __init__(self, queue):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel = self.connection.channel()
        self.queue = queue

    def send(self, body):
        self.channel.basic_publish(exchange='', routing_key=self.queue, body=body)

    def consuming(self, callback):
        self.channel.basic_consume(queue=self.queue,
                                   auto_ack=True,
                                   on_message_callback=callback)
        self.channel.start_consuming()