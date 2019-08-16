# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, location, inventory):
        self.name = name
        self.location = location
        self.inventory = inventory

    def change_location(self, direction):
        direction = direction.upper()
        try:
            if direction == "N":
                self.location = self.location.n_to
            elif direction == "S":
                self.location = self.location.s_to
            elif direction == "E":
                self.location = self.location.e_to
            elif direction == "W":
                self.location = self.location.w_to
            else:
                print("Please input a cardinal direction, or q to quit")
        except AttributeError:
            print("You can't go that way")

    def take_item(self, item):
        new_item = self.location.rem_item(item)
        if new_item == False:
            print("No item by that description is here")
        else:
            self.inventory.append(new_item)

    def drop_item(self, item):
        self.inventory.rem_item(item)
        self.location.append(item)
