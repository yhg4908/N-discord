import asyncio
import json
import websockets

DISCORD_GATEWAY_URL = "wss://gateway.discord.gg/?v=10&encoding=json"

class Gateway:
    def __init__(self, token, intents):
        self.token = token
        self.intents = intents
        self.websocket = None
        self.heartbeat_interval = None
        self.sequence = None

    async def connect(self):
        try:
            print("Connecting to Discord Gateway...")
            self.websocket = await websockets.connect(DISCORD_GATEWAY_URL)
            await self._identify()
            await self._listen()
        except Exception as e:
            print(f"An error occurred while connecting to the Gateway: {e}")

    async def _identify(self):
        payload = {
            "op": 2,  # Identify opcode
            "d": {
                "token": self.token,
                "intents": self.intents.value,  # 인텐트를 포함
                "properties": {
                    "$os": "linux",
                    "$browser": "discordlite",
                    "$device": "discordlite"
                }
            }
        }
        await self.websocket.send(json.dumps(payload))
        print("Sent IDENTIFY payload with intents to Discord Gateway.")

    async def _listen(self):
        async for message in self.websocket:
            event = json.loads(message)
            op = event.get("op")
            t = event.get("t")
            d = event.get("d")
            self.sequence = event.get("s")

            # Heartbeat Ack
            if op == 10:
                self.heartbeat_interval = d["heartbeat_interval"] / 1000
                print(f"Heartbeat interval received: {self.heartbeat_interval}s")
                asyncio.create_task(self._heartbeat())

            # 기타 이벤트 처리
            if t:
                print(f"Received event: {t}")

    async def _heartbeat(self):
        while True:
            await asyncio.sleep(self.heartbeat_interval)
            payload = {"op": 1, "d": self.sequence}
            await self.websocket.send(json.dumps(payload))
            print("Sent Heartbeat to Discord Gateway.")
