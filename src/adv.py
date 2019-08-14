import textwrap
from room import Room
from player import Player

wrapper = textwrap.TextWrapper(width=50)

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

hero = Player("Norm", room["outside"])
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

while True:
    print("\n", hero.location.name)
    description = wrapper.wrap(text=hero.location.description)
    for i in description:
        print(i)

    p_input = input("Which direction would you like to go?: ")
    check_input = p_input.upper()

    try:
        if check_input == "Q":
            break
        elif check_input == "N":  # move north
            hero.change_location(hero.location.n_to)
        elif check_input == "S":  # move south
            hero.change_location(hero.location.s_to)
        elif check_input == "E":  # move east
            hero.change_location(hero.location.e_to)
        elif check_input == "W":  # move west
            hero.change_location(hero.location.w_to)
        else:
            print("Please input a cardinal direction, or q to quit")

    except AttributeError:
        print("You try to walk through the wall, but it just isn't happening")
