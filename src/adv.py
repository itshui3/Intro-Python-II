from roomgen import room
from player import Player
from classes import Warrior, Thief, Mage

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

    elif command == 'search':
        # if items exist, search for them
        pass

    elif command == 'attack':
        # if monster(s) exist, attack [if more than one monster, setup input retrieval for which to attack]
        pass

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
