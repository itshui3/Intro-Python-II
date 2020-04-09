from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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
playerName = input('Enter a player name: ')
newPlayer = Player(playerName, room['outside'])

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

if(playerName == 'Admin'):
    while True:
        adminInput = input('Input Commands: ')

        #Item Interface
        if(adminInput == 'items'):
            input('Item Interface: ')
            continue
        
        #Quit config interface
        if(adminInput == 'q' or adminInput == 'Q'):

            cont = input('Done with admin configurations! Now try it out? [yes/no] ')

            if(cont == 'yes'):
                break
            else:
                quit()

while True:
    print(newPlayer.getLocation())
    userInput = input('Input Action: ')

    #Movement interface
    if(userInput == 'n' or userInput == 'N'):
        try:
            newPlayer.setLocation(newPlayer.getLocation().n_to)
        except:
            print('No room to the north of player location')
        continue

    if(userInput == 'e' or userInput == 'E'):
        try:
            newPlayer.setLocation(newPlayer.getLocation().e_to)
        except:
            print('No room to the north of player location')
        continue

    if(userInput == 's' or userInput == 'S'):
        try:
            newPlayer.setLocation(newPlayer.getLocation().s_to)
        except:
            print('No room to the north of player location')
        continue

    if(userInput == 'w' or userInput == 'W'):
        try:
            newPlayer.setLocation(newPlayer.getLocation().w_to)
        except:
            print('No room to the north of player location')
        continue


    if(userInput == 'q' or userInput == 'Q'):
        print(userInput)
        break

    #items interface