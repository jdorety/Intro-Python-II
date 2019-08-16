# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.items = items

    def rem_item(self, item):

        try:
            items = [i.name.lower() for i in self.items]
            item = item.lower()

            if item in items:
                index = items.index(item)
                get_it = self.items[index]
                self.items.remove(self.items[index])
                return get_it

            else:
                return False

        except(ValueError):
            print("Item does not exist")

    def add_item(self, item):
        self.items.append(item)
