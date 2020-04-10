class Monster:
    def __init__(self, name, description, hp, ap):
        self.name = name
        self.description = description
        self.hp = hp
        self.ap = ap

    def __str__(self):
        return '[Enemy: ' + self.name + ']: ' + self.description