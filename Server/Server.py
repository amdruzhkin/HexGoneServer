import asyncio
import websockets

from Core import Core
from Consumer import Consumer
from Producer import Producer

class Server:
    def __init__(self):
        self.Core = Core()
        self.Consumer = Consumer(self.Core)
        self.Producer = Producer(self.Core)

    def run(self, ip, port):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(websockets.serve(self.handler, ip, port))
        loop.run_forever()

    async def handler(self, ws):
        cons = asyncio.ensure_future(self.Consumer.handler(ws))
        core = asyncio.ensure_future(self.Core.handler())
        prod = asyncio.ensure_future(self.Producer.handler())

        done, pending = await asyncio.wait(
            [cons, core, prod],
            return_when=asyncio.FIRST_COMPLETED,
        )
        for task in pending:
            task.cancel()
