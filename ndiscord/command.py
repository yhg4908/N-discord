class CommandOption:
    def __init__(self, name, description, category, essential):
        self.name = name
        self.description = description
        self.category = category
        self.essential = essential

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "type": self._get_type(),
            "required": self.essential,
        }

    def _get_type(self):
        type_map = {
            "user": 6,
            "text": 3,
            "number": 10,
            "channel": 7,
            "category": 7,  
        }
        return type_map.get(self.category, 3)  


class Command:
    def __init__(self, name, description, func):
        self.name = name
        self.description = description
        self.func = func
        self.options = []

    def option(self, name, description, category, essential):
        option = CommandOption(name, description, category, essential)
        self.options.append(option)
        return self
      
    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "options": [opt.to_dict() for opt in self.options],
        }
