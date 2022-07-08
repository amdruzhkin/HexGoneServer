import asyncio
import json

from Utils.RabbitMQ import RabbitMQ


class Consumer:
    def __init__(self, core):
        self.Core = core

    async def handler(self, ws):
        await self.register(ws)

        try:
            async for message in ws:
                message = json.loads(message)
                message["sender"] = hex(id(ws))
                self.Core.i_stream.append(json.dumps(message))


        except Exception as e:
            await self.unregister(ws)
            print(e)
        finally:
            await self.unregister(ws)

        await asyncio.sleep(0)

    async def register(self, ws):
        try:
            self.Core.connections[hex(id(ws))] = ws
            print(f"New connection: { ws.remote_address[0] }:{ ws.remote_address[1] }")
        except Exception as e:
            print(e)

    async def unregister(self, ws):
        try:
            del self.Core.connections[hex(id(ws))]
            print(f"Connection closed: {ws.remote_address[0]}:{ws.remote_address[1]}")
        except Exception as e:
            print(e)