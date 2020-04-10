class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return '[Item: ' + f"{self.name}]: " + self.description

    def getName(self):
        return self.name

class Utility(Item):
    def __init__(self, name, description):
        super().__init__(name, description)
        self.type = 'Utility'

class Combat(Item):
    def __init__(self, name, description):
        super().__init__(name, description)
        self.type = 'Combat'

class Weapon(Combat):
    def __init__(self, name, description, offense):
        super().__init__(name, description)
        self.offense = offense

class Armor(Combat):
    def __init__(self, name, description, offense):
        super().__init__(name, description)
        self.defense = defense

# composition solves inflexibility issue with class inheritance
