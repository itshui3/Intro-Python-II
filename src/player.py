# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, location, items=None):
        self.name = name
        self.location = location
        if(items is None):
            self.items = []
        else:
            self.items = items
    
    def getLocation(self):
        return self.location
    
    def setLocation(self, newLocation):
        self.location = newLocation