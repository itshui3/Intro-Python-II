from room import Room
from player import Player
from classes import Warrior, Thief, Mage

# Declare all the rooms

room = {
    'outside': Room("Outside Cave Entrance", "North of you, the cave mount beckons"),

    'foyer': Room("Foyer", """Dim light filters in from the south. Dusty passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm."""),

    'narrow': Room("Narrow Passage", """The narrow passage bends here from west to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south."""),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = None

while True:
# Character Creation
    if player == None:
        name = input('Welcome to Adv Game, pick a name.\n')
        job = input(f'Great, {name}! Now pick a job. [Warrior, Thief, Mage]\n')

        jobs = {
            'Warrior': Warrior,
            'Thief': Thief,
            'Mage': Mage
        }

        if job in jobs:
            player = Player(name, room['outside'], jobs[job])
            print(f'You have successfully created a character. You are a {player.job}.')
        else:
            print('Not a valid job')
            continue
# Game-Start
    print(f'{player.current_room}')
    command = input('\nSelect a Command: [\'move\', \'attack\', \'search\', \'q\']\n')

    if command == 'move':
        # if monster exists, prevent movement

        print(' ' * 33 + 'n\n' + 'Select a direction to move in: w   e\n' + ' ' * 33 + 's')

        direction = input()
        direction = direction + '_to'
        if hasattr(player.current_room, direction):
            player.current_room = getattr(player.current_room, direction)
            continue
        else:
            print('No Room in that direction')
            continue

    elif command == 'q':
        print('Thanks for playing!')
        break

    
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
