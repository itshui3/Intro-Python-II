import os
import sys

entities = os.path.abspath( os.path.dirname( __file__ ) + '/entities' )
sys.path.insert( 0, entities )

from mobs import Monster

print(Monster)