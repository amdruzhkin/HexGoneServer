import asyncio
import json

from Utils.RabbitMQ import RabbitMQ


class Consumer:
    def __init__(self, connections):
        self.connections = connections
        self.services = self._init_services()


    async def handler(self, ws):
        await self.register(ws)

        try:
            async for message in ws:
                data = json.loads(message)
                data["sender"] = hex(id(ws))
                self.services[data["service"]].send(json.dumps(data))

        except Exception as e:
            await self.unregister(ws)
            print(e)
        finally:
            await self.unregister(ws)

        await asyncio.sleep(0)

    async def register(self, ws):
        try:
            self.connections[hex(id(ws))] = ws
            print(f"New connection: { ws.remote_address[0] }:{ ws.remote_address[1] }")
        except Exception as e:
            print(e)

    async def unregister(self, ws):
        try:
            del self.connections[hex(id(ws))]
            print(f"Connection closed: {ws.remote_address[0]}:{ws.remote_address[1]}")
        except Exception as e:
            print(e)

    def _init_services(self):
        return {
            "GameManager": RabbitMQ("GameManager"),
        }