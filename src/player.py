# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, location, hp, items=None):
        self.name = name
        self.location = location
        self.hp = hp
        if(items is None):
            self.items = []
        else:
            self.items = items
        
    
    def getLocation(self):
        return self.location

    def getNearbyEnemies(self):
        return self.location.returnEnemies()
    
    def setLocation(self, newLocation):
        self.location = newLocation

    def removeItem(self, item):
        self.items.remove

    def dropItem(self, item):
        for storedItem in self.items:
            if(storedItem.getName() == item):
                self.items.remove(storedItem)
                self.location.addItem(storedItem)
                print('\Dropped an item!\n', item)

    def checkItems(self):
        return self.items

    def loot(self, item):
        for roomItem in self.getLocation().items:
            if(roomItem.getName() == item):
                self.items.append(roomItem)
                self.getLocation().removeItem(roomItem)
                print('\nObtained an item!\n', item)