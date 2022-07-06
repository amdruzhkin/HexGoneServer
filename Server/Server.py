import asyncio
import websockets
import threading

from Consumer import Consumer
from Producer import Producer


class Server:
    def __init__(self):
        self.connections = dict()
        self.Consumer = Consumer(self.connections)
        self.Producer = Producer(self.connections)

    def run(self, ip, port):
        loop = asyncio.get_event_loop()
        threading.Thread(target=self.Producer.handler).start()
        loop.run_until_complete(websockets.serve(self.handler, ip, port))
        loop.run_forever()

    async def handler(self, ws):
        consumer_task = asyncio.ensure_future(self.Consumer.handler(ws))

        done, pending = await asyncio.wait(
            [consumer_task],
            return_when=asyncio.FIRST_COMPLETED,
        )
        for task in pending:
            task.cancel()
