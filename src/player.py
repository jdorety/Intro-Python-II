# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, location, inventory):
        self.name = name
        self.location = location
        self.inventory = inventory

    def change_location(self, new_location):
        self.location = new_location

    def take_item(self, item):
        self.location.rem_item(item)
        self.inventory.append(item)
