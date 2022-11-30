class Pokemon:
    def __init__(self, pokemon, force, health, type):
        self.pokemon = pokemon
        self.force = force
        self.health = health
        self.type = type
        self.maxhealth = health
    def __str__(self):
        return f"{self.pokemon} é do tipo {self.type} e tem {self.force} de força e {self.health} de vida."

class Trainer:
    def __init__(self, name, type, poke1, poke2, poke3, badge):
        self.name = name
        self.type = type
        self.poke1 = poke1
        self.poke2 = poke2
        self.poke3 = poke3
        self.badge = badge
    def __str__(self):
        return f"{self.name} é um líder de ginásio do tipo {self.type}. Ele usa os pokémon: {self.poke1}, {self.poke2}, {self.poke3}. Ao ser derrotado, ele dá a insígnia {self.badge}."