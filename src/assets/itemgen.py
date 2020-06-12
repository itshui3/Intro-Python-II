import sys
import os

entities = os.path.abspath( os.path.dirname( __file__ ) + '/entities' )
sys.path.insert( 0, entities )

from items import Weapon, Potion, Armor

print( Weapon )