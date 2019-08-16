from item import Item


class LightSource(Item):
    def __init__(self, name, description, activated=False):
        super().__init__(name, description)
        self.light_source = True
        self.activated = activated

    def __str__(self):
        power = "on" if self.activated else "off"
        return f"The {self.name} is {power}"

    def on_drop(self):
        print(f"You probably shoudn't drop this {self.name}")
