import asyncio
import json

from GameManager.GameManager import GameManager


class Core:
    def __init__(self):
        self.connections = dict()
        self.i_stream = []
        self.o_stream = []
        self.services = self._services()

    async def handler(self):
        while True:
            if len(self.i_stream) > 0:
                message = json.loads(self.i_stream.pop())
                service = message["service"]
                del message["service"]
                o_data = await self.services[service].handle(message)
                self.o_stream.append(json.dumps(o_data))
            await asyncio.sleep(0)

    def _services(self):
        return {
            "GameManager": GameManager()
        }