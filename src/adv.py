import textwrap
from room import Room
from item import Item
from player import Player

wrapper = textwrap.TextWrapper(width=50)
play = True


# Declare all the rooms
amulet = Item("Amulet", "Revives the wearer's beloved")
trident = Item("Trident", "King Triton's prized posession")

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [amulet, trident]),

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

hero = Player("Norm", room["outside"], ["wood shield", "Sword of Might"])
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


# def parse(in_string):
#     command = in_string.upper()
#     command = command.split()
#     count = len(command)

#     if count == 1:
#         command = command[0]
#     elif count > 1


#     return count

def move(direction, player):
    global play
    try:
        if check_input == "Q":
            play = False
        elif check_input == "N":  # move north
            player.change_location(player.location.n_to)
        elif check_input == "S":  # move south
            player.change_location(player.location.s_to)
        elif check_input == "E":  # move east
            player.change_location(player.location.e_to)
        elif check_input == "W":  # move west
            player.change_location(player.location.w_to)
        else:
            print("Please input a cardinal direction, or q to quit")

    except AttributeError:
        print("You try to walk through the wall, but it just isn't happening")


while play == True:
    print("\n" + hero.location.name)
    description = wrapper.wrap(text=hero.location.description)
    for i in description:
        print(i)

    if hero.location.items:
        for i in hero.location.items:
            print(i.name)

    p_input = input("Which direction would you like to go?: ")
    # print(parse(p_input))
    check_input = p_input.upper()
    move(check_input, hero)