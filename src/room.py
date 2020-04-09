# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items=None):
        self.name = name
        self.description = description
        if(items is None):
            self.items = []
        else:
            self.items = items

    def __str__(self):
        return 'Current Location: ' + self.name + '. ' + self.description