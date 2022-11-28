class Pokemon:
    def __init__(self, pokemon, force, health, type):
        self.pokemon = pokemon
        self.force = force
        self.health = health
        self.type = type
    def __str__(self):
        return f"{self.pokemon} is a {self.type} with {self.force} and {self.health} health."