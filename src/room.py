# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.items = items

    def rem_item(self, item):
        try:
            self.items.remove(item)
        except(ValueError):
            print("Item does not exist")

    def add_item(self, item):
        self.items.append(item)



