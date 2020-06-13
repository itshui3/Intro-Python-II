import os
import sys

sys.path.insert( 0, os.path.abspath( os.path.dirname( __file__ ) + '/entities' ) )

from mobs import Monster

monsterlist = {
    # 'name': ['Name', 'Description', int(hp), int(atk)],
    'goblin': ['Goblin', 'An ugly green creature ranging between the size of a hobbit or dwarf to a human', 15, 3],
    'slime': ['Slime', 'A gelatinous substance', 25, 1]
}

monsters = {

    'goblin': Monster( *monsterlist['goblin'] ),
    'slime': Monster( *monsterlist['slime'] )
    
}