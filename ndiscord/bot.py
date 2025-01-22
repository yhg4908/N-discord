import asyncio
from .gateway import Gateway
from .command import Command

class Bot:
    def __init__(self, intents=None):
        self.token = None
        self.gateway = None
        self.intents = intents
        self.commands = []

    def command(self, name, description):
        def decorator(func):
            command = Command(name, description, func)
            self.commands.append(command)
            return command
        return decorator

    def start(self, token):
        self.token = token
        if not self.token:
            raise ValueError("Token must be provided to start the bot.")

        print(f"Starting bot with token: {self.token[:5]}******")
        self.gateway = Gateway(self.token, self.intents)
        asyncio.run(self._run())

    async def _run(self):
        await self._sync_commands()
        await self.gateway.connect()

    async def _sync_commands(self):
        print(f"Synchronizing {len(self.commands)} commands with Discord...")
        for cmd in self.commands:
            print(f"Synced command: {cmd.name} with options: {[opt.name for opt in cmd.options]}")
