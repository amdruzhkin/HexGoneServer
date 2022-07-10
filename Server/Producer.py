import asyncio
import json


class Producer():
    def __init__(self, core):
        self.Core = core

    async def handler(self):
        while True:
            if len(self.Core.o_stream) > 0:
                message = json.loads(self.Core.o_stream.pop())
                recipients = message["recipients"]
                del message["recipients"]
                for r in recipients:
                    await self.Core.connections[r].send(json.dumps(message))
            await asyncio.sleep(0)


