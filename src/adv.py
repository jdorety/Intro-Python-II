# I keep forgetting to branch at the start

import textwrap
from room import Room
from item import Item
from lightsource import LightSource
from player import Player

wrapper = textwrap.TextWrapper(width=50)
play = True


# Declare all the rooms
amulet = Item("Amulet", "Revives the wearer's beloved")
trident = Item("Trident", "King Triton's prized posession")
torch = LightSource("Torch", "a wooden torch", True)

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [torch]),

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
shield = Item("Shield", "Wooden Shielf")
sword = Item("Sword", "Sword of might!")
hero = Player("Norm", room["outside"], [shield, sword])
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

def print_items(room):
    if len(room.items) > 0:

        items = [i.name for i in room.items]
        vowel = "an" if items[0][0].lower() in (
            "a", "e", "i", "o", "u") else "a"

        if len(items) == 1:
            print(f"You see {vowel} {items[0]}")
        if len(items) == 2:
            print(f"You see {vowel} {items[0]} and {items[1]}")
        elif len(items) > 2:
            items[-1] = f"and {items[-1]}"
            end = ", ".join(items)
            print(f"You see {vowel}", end)

    else:
        return


def parse(choice, player):
    c_list = choice.split(" ")

    # No command is input
    if len(c_list) < 1:
        print("Please input a command")

    # One word inputs
    elif len(c_list) == 1:
        command = c_list[0].upper()
        if command in ('I', 'INV', 'INVENTORY'):
            player.show_inv()
        else:
            player.change_location(command)

    # Multiple word inputs
    else:
        verb = c_list[0].upper()
        noun = c_list[1].lower()
        if verb in ("TAKE", "GET"):
            player.take_item(noun)  # take item method
        elif verb == "DROP":
            player.drop_item(noun)  # drop item method
        else:
            print("I don't understand")


while play == True:
    print("\n" + hero.location.name)

    description = wrapper.wrap(text=hero.location.description)
    for i in description:
        print(i)

    print_items(hero.location)
    p_input = input("What would you like to do?: ")

    if p_input.upper() in ("Q", "QUIT", "EXIT"):
        play = False
        break

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
    parse(p_input, hero)
