class Monster():
    def __init__(self, name, description, hp, atk):
        self.name = name
        self.description = description
        self.hp = hp
        self.atk = atk

    def __repr__(self):
        return '{' + f'name: {self.name}, description: {self.description}, hp: {self.hp}, atk: {self.atk}' + '}'
        
    def __str__(self):
        return f'Name: {self.name}\nDescription: {self.description}\nHP: {self.hp}\nATK: {self.atk}'