class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name}"

    def on_take(self):
        print(f"You pick up the {self.name}")

    def on_drop(self):
        print(f"You drop the {self.name}")
