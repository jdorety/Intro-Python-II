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
                print("I'm afraid I can't do that")

        except AttributeError:
            print("You can't go that way")

    def show_inv(self):
        inv = [i.name for i in self.inventory]
        print("You are carrying:")
        for i in inv:
            print(i)

    def take_item(self, item):
        get_it = self.location.rem_item(item)

        if get_it == False:
            print("No item by that description is here")
        else:
            self.inventory.append(get_it)
            get_it.on_take()

    def drop_item(self, item):
        item = item.lower()
        inv = [i.name.lower() for i in self.inventory]

        if item in inv:
            index = inv.index(item)
            get_it = self.inventory[index]
            self.inventory.remove(self.inventory[index])
            self.location.add_item(get_it)
            get_it.on_drop()
        else:
            print("What?")
