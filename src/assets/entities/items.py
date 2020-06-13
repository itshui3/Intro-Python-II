class Item():
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return '{' + f'name: {self.name}, description: {self.description}' + '}'

class Weapon(Item):
    def __init__(self, name, description, atk, job):
        super().__init__(name, description)
        self.atk = atk
        self.job = job
        # if job matches player's job, special attack enabled

    def __repr__(self):
        return '{' + f'name: {self.name}, description: {self.description}, atk: {self.atk}, job: {self.job}' + '}'

    def __str__(self):
        return f'[Weapon]\nName: {self.name}\nAtk: {self.atk}\nDescription: {self.description}\nFor: {str(self.job)}'

class Armor(Item):
    def __init__(self, name, description, defense):
        super().__init__(name, description)
        self.defense = defense

    def __repr__(self):
        return '{' + f'name: {self.name}, description: {self.description}, defense: {self.defense}'

    def __str__(self):
        return f'[Armor]\nName: {self.name}\nDefense: {self.defense}\nDescription: {self.description}'

class Potion(Item):
    def __init__(self, name, description, heals):
        super().__init__(name, description)
        self.heals = heals

    def __repr__(self):
        return '{' + f'name: {self.name}, description: {self.description}, heals: {self.heals}' + '}'

    def __str__(self):
        return f'[Potion]\nName: {self.name}\nHeals For: {self.heals}\nDescription: {self.description}'