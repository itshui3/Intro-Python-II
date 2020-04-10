# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items=None, enemies=None):

        self.name = name
        self.description = description

        if(items is None):
            self.items = []
        else:
            self.items = items

        if(enemies is None):
            self.enemies = []
        else:
            self.enemies = enemies

    def __str__(self):
        return 'Current Location: ' + self.name + '. ' + self.description

    def removeItem(self, item):
        self.items.remove(item)

    def addItem(self, item):
        self.items.append(item)

    def addEnemy(self, enemy):
        self.enemies.append(enemy)

    def returnEnemies(self):
        return self.enemies

    def returnItems(self):
        for item in self.items:
            print(item)
    
    def returnItem(self, index):
        return self.items[index]