import sys
import os

# sys.path.insert( 0, os.path.abspath( os.path.dirname( __file__ ) + '/entities' ) )
# sys.path.insert( 0, os.path.abspath( os.path.dirname( __file__ ) + '/resources' ) )

from items import Weapon, Potion, Armor

itemParts = {
# weaponry
    'axe': ['Axe', 'A hefty leather handled axe', 10, 'Warrior'],
    'sword': ['Sword', 'A steel sword', 7, 'Warrior'],
    'wand': ['Wand', 'An old wand', 3, 'Mage'],
# armor
    'breastplate': ['Breastplate', 'Metal plate worn as defensive armor for the breast', 5],
    'fullplate': ['Full Plate', 'A suit of steel armor that when worn encases the wearer', 15],
# potions
    'redpotion': ['Red Potion', 'A common potion capable of restoring health points', 12],
    'greenpotion': ['Green Potion', 'An uncommon potion used to heal wounds', 20],
    'yellowpotion': ['Yellow Potion', 'A strong potion, capable of curing grievious wounds', 35]
}

weapons = {

    'axe': Weapon( *itemParts['axe'] ),
    'sword': Weapon( *itemParts['sword'] ),
    'wand': Weapon( *itemParts['wand'] )

}

armor = {

    'breastplate': Armor( *itemParts['breastplate'] ),
    'fullplate': Armor( *itemParts['fullplate'] ),

}

potions = {

    'redpotion': Potion( *itemParts['redpotion'] ),
    'greenpotion': Potion( *itemParts['greenpotion'] ),
    'yellowpotion': Potion( *itemParts['yellowpotion'] )

}