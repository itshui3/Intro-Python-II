class Warrior():
    def __init__(self, hp=50, atk=10):
        self.hp = hp
        self.atk = atk

    def bash(self):
        return self.atk * 1.4

    def __repr__(self):
        return '{' + f'hp: {self.hp}, atk: {self.atk}' + '}'

    def __str__(self):
        return 'Warrior'

    # I need to modify bash with atk + weapon dmg, but weapon dmg is external(?)

class Thief():
    def __init__(self, hp=38, atk=12):
        self.hp = hp
        self.atk = atk

    def doublestrike(self):
        return self.atk * 2

    def __repr__(self):
        return '{' + f'hp: {self.hp}, atk: {self.atk}' + '}'

    def __str__(self):
        return 'Thief'

class Mage():
    def __init__(self, hp=25, atk=15):
        self.hp = hp
        self.atk = atk

    def firebolt(self):
        return self.atk * 1.8

    def __repr__(self):
        return '{' + f'hp: {self.hp}, atk: {self.atk}' + '}'

    def __str__(self):
        return 'Mage'