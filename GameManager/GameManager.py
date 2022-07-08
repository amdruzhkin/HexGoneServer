import threading
import time


class GameManager:
    def __init__(self):
        self.actions = self._init_actions()
        self.queue = set()

        threading.Thread(target=self.processor).start()

    def processor(self):
        while True:
            print("Processor")
            time.sleep(5)

    async def handle(self, message):
        action = message["action"]
        sender = message["sender"]
        del message["action"]
        return await self.actions[action](sender)

    def _init_actions(self):
        return {
            "join_queue": self.join_queue,
            "quit_queue": self.quit_queue,
        }

    async def join_queue(self, sender):
        self.queue.add(sender)
        return {
            "action": "join_queue",
            "recipients": [sender],
            "status": "accept",
        }

    async def quit_queue(self, sender):
        try:
            self.queue.remove(sender)
            return {
                "action": "quit_queue",
                "recipients": [sender],
                "status": "success",
            }
        except Exception as e:
            return {
                "action": "quit_queue",
                "recipients": [sender],
                "status": "failed",
            }


