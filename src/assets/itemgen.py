import sys
import os

items = os.path.abspath( os.path.dirname(__file__) + '/entities' )
sys.path.insert(0, items)


from items import Weapon, Potion, Armor

print(Weapon)