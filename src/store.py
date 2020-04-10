class DrinkStation:
    def __init__(self, name, inventory=None):
        self.name = name
        if(inventory is None):
            self.inventory = []
        else:
            self.inventory = inventory

class Drink:
    def __init__(self, name):
        self.name = name
      
