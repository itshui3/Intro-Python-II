class Warrior():
    def __init__(self, hp=50, atk=10):
        self.hp = hp
        self.atk = atk

    def attack(self, weapon, target):
        # calculate attack based on weapon, target, and class
        # return a combat result interface with information that can get rendered back to repl
        pass

    def __repr__(self):
        return '{' + f'hp: {self.hp}, atk: {self.atk}' + '}'

    def __str__(self):
        return 'Warrior'

    # I need to modify bash with atk + weapon dmg, but weapon dmg is external(?)

class Thief():
    def __init__(self, hp=38, atk=12):
        self.hp = hp
        self.atk = atk

    def attack(self, weapon, target):
        # calculate attack based on weapon, target, and class
        # return a combat result interface with information that can get rendered back to repl
        pass

    def __repr__(self):
        return '{' + f'hp: {self.hp}, atk: {self.atk}' + '}'

    def __str__(self):
        return 'Thief'

class Mage():
    def __init__(self, hp=25, atk=15):
        self.hp = hp
        self.atk = atk

    def attack(self, weapon, target):
        # calculate attack based on weapon, target, and class
        # return a combat result interface with information that can get rendered back to repl
        pass

    def __repr__(self):
        return '{' + f'hp: {self.hp}, atk: {self.atk}' + '}'

    def __str__(self):
        return 'Mage'