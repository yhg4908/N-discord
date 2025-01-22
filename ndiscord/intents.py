class Intents:
    DEFAULT = 0  # 기본값, 아무 이벤트도 수신하지 않음
    GUILDS = 1 << 0
    GUILD_MEMBERS = 1 << 1
    GUILD_BANS = 1 << 2
    GUILD_EMOJIS_AND_STICKERS = 1 << 3
    GUILD_INTEGRATIONS = 1 << 4
    GUILD_WEBHOOKS = 1 << 5
    GUILD_INVITES = 1 << 6
    GUILD_VOICE_STATES = 1 << 7
    GUILD_PRESENCES = 1 << 8
    GUILD_MESSAGES = 1 << 9
    GUILD_MESSAGE_REACTIONS = 1 << 10
    GUILD_MESSAGE_TYPING = 1 << 11
    DIRECT_MESSAGES = 1 << 12
    DIRECT_MESSAGE_REACTIONS = 1 << 13
    DIRECT_MESSAGE_TYPING = 1 << 14
    MESSAGE_CONTENT = 1 << 15
    AUTO_MODERATION_CONFIGURATION = 1 << 20
    AUTO_MODERATION_EXECUTION = 1 << 21
    ALL = (
        GUILDS
        | GUILD_MEMBERS
        | GUILD_BANS
        | GUILD_EMOJIS_AND_STICKERS
        | GUILD_INTEGRATIONS
        | GUILD_WEBHOOKS
        | GUILD_INVITES
        | GUILD_VOICE_STATES
        | GUILD_PRESENCES
        | GUILD_MESSAGES
        | GUILD_MESSAGE_REACTIONS
        | GUILD_MESSAGE_TYPING
        | DIRECT_MESSAGES
        | DIRECT_MESSAGE_REACTIONS
        | DIRECT_MESSAGE_TYPING
        | MESSAGE_CONTENT
        | AUTO_MODERATION_CONFIGURATION
        | AUTO_MODERATION_EXECUTION
    )

    def __init__(self, **kwargs):
        self.value = 0
        for intent, enabled in kwargs.items():
            if enabled:
                self.value |= getattr(self, intent.upper(), 0)

    def enable(self, intent_name):
        """Enable a specific intent by name."""
        self.value |= getattr(self, intent_name.upper(), 0)

    def disable(self, intent_name):
        """Disable a specific intent by name."""
        self.value &= ~getattr(self, intent_name.upper(), 0)

    def has_intent(self, intent_name):
        """Check if a specific intent is enabled."""
        return bool(self.value & getattr(self, intent_name.upper(), 0))
