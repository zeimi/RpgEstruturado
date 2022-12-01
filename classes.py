class Pokemon:
    attackDict = {'Normal': {'Normal': 1, 'Fogo': 1, 'Água': 1, 'Planta': 1, 'Elétrico': 1, 'Gelo': 1, 'Lutador': 1, 'Venenoso': 1, 'Terra': 1, 'Voador': 1, 'Psíquico': 1, 'Inseto': 1, 'Pedra': 0.5, 'Fantasma': 0, 'Dragão': 1, 'Noturno': 1, 'Metal': 0.5, 'Fada': 1},
                'Fogo': {'Normal': 1, 'Fogo': 0.5, 'Água': 0.5, 'Planta': 2, 'Elétrico': 1, 'Gelo': 2, 'Lutador': 1, 'Venenoso': 1, 'Terra': 1, 'Voador': 1, 'Psíquico': 1, 'Inseto': 2, 'Pedra': 0.5, 'Fantasma': 1, 'Dragão': 0.5, 'Noturno': 1, 'Metal': 2, 'Fada': 1},
                'Água': {'Normal': 1, 'Fogo': 2, 'Água': 0.5, 'Planta': 0.5, 'Elétrico': 2, 'Gelo': 1, 'Lutador': 1, 'Venenoso': 1, 'Terra': 2, 'Voador': 1, 'Psíquico': 1, 'Inseto': 1, 'Pedra': 2, 'Fantasma': 1, 'Dragão': 0.5, 'Noturno': 1, 'Metal': 1, 'Fada': 1},
                'Planta': {'Normal': 1, 'Fogo': 0.5, 'Água': 2, 'Planta': 0.5, 'Elétrico': 0.5, 'Gelo': 1, 'Lutador': 1, 'Venenoso': 0.5, 'Terra': 2, 'Voador': 0.5, 'Psíquico': 1, 'Inseto': 0.5, 'Pedra': 2, 'Fantasma': 1, 'Dragão': 0.5, 'Noturno': 1, 'Metal': 0.5, 'Fada': 1},
                'Elétrico': {'Normal': 1, 'Fogo': 1, 'Água': 2, 'Planta': 0.5, 'Elétrico': 0.5, 'Gelo': 1, 'Lutador': 1, 'Venenoso': 1, 'Terra': 0, 'Voador': 2, 'Psíquico': 1, 'Inseto': 1, 'Pedra': 1, 'Fantasma': 1, 'Dragão': 0.5, 'Noturno': 1, 'Metal': 1, 'Fada': 1},
                'Gelo': {'Normal': 1, 'Fogo': 0.5, 'Água': 0.5, 'Planta': 2, 'Elétrico': 1, 'Gelo': 0.5, 'Lutador': 1, 'Venenoso': 1, 'Terra': 2, 'Voador': 2, 'Psíquico': 1, 'Inseto': 1, 'Pedra': 1, 'Fantasma': 1, 'Dragão': 2, 'Noturno': 1, 'Metal': 0.5, 'Fada': 1},
                'Lutador': {'Normal': 2, 'Fogo': 1, 'Água': 1, 'Planta': 1, 'Elétrico': 1, 'Gelo': 2, 'Lutador': 1, 'Venenoso': 0.5, 'Terra': 1, 'Voador': 0.5, 'Psíquico': 0.5, 'Inseto': 0.5, 'Pedra': 2, 'Fantasma': 0, 'Dragão': 1, 'Noturno': 2, 'Metal': 2, 'Fada': 0.5},
                'Venenoso': {'Normal': 1, 'Fogo': 1, 'Água': 1, 'Planta': 2, 'Elétrico': 1, 'Gelo': 1, 'Lutador': 1, 'Venenoso': 0.5, 'Terra': 0.5, 'Voador': 1, 'Psíquico': 1, 'Inseto': 1, 'Pedra': 0.5, 'Fantasma': 0.5, 'Dragão': 1, 'Noturno': 1, 'Metal': 0, 'Fada': 2},
                'Terra': {'Normal': 1, 'Fogo': 2, 'Água': 1, 'Planta': 0.5, 'Elétrico': 2, 'Gelo': 1, 'Lutador': 1, 'Venenoso': 2, 'Terra': 1, 'Voador': 0, 'Psíquico': 1, 'Inseto': 0.5, 'Pedra': 2, 'Fantasma': 1, 'Dragão': 1, 'Noturno': 1, 'Metal': 2, 'Fada': 1},
                'Voador': {'Normal': 1, 'Fogo': 1, 'Água': 1, 'Planta': 2, 'Elétrico': 0.5, 'Gelo': 1, 'Lutador': 2, 'Venenoso': 1, 'Terra': 1, 'Voador': 1, 'Psíquico': 1, 'Inseto': 2, 'Pedra': 0.5, 'Fantasma': 1, 'Dragão': 1, 'Noturno': 1, 'Metal': 0.5, 'Fada': 1},
                'Psíquico': {'Normal': 1, 'Fogo': 1, 'Água': 1, 'Planta': 1, 'Elétrico': 1, 'Gelo': 1, 'Lutador': 2, 'Venenoso': 2, 'Terra': 1, 'Voador': 1, 'Psíquico': 0.5, 'Inseto': 1, 'Pedra': 1, 'Fantasma': 1, 'Dragão': 1, 'Noturno': 0, 'Metal': 0.5, 'Fada': 1},
                'Inseto': {'Normal': 1, 'Fogo': 0.5, 'Água': 1, 'Planta': 2, 'Elétrico': 1, 'Gelo': 1, 'Lutador': 0.5, 'Venenoso': 0.5, 'Terra': 1, 'Voador': 0.5, 'Psíquico': 2, 'Inseto': 1, 'Pedra': 2, 'Fantasma': 0.5, 'Dragão': 1, 'Noturno': 2, 'Metal': 0.5, 'Fada': 0.5},
                'Pedra': {'Normal': 1, 'Fogo': 2, 'Água': 1, 'Planta': 1, 'Elétrico': 1, 'Gelo': 2, 'Lutador': 0.5, 'Venenoso': 1, 'Terra': 0.5, 'Voador': 2, 'Psíquico': 1, 'Inseto': 2, 'Pedra': 1, 'Fantasma': 1, 'Dragão': 1, 'Noturno': 1, 'Metal': 0.5, 'Fada': 1},                    
                'Fantasma': {'Normal': 0, 'Fogo': 1, 'Água': 1, 'Planta': 1, 'Elétrico': 1, 'Gelo': 1, 'Lutador': 1, 'Venenoso': 1, 'Terra': 1, 'Voador': 1, 'Psíquico': 2, 'Inseto': 1, 'Pedra': 1, 'Fantasma': 2, 'Dragão': 1, 'Noturno': 0.5, 'Metal': 1, 'Fada': 1},
                'Dragão': {'Normal': 1, 'Fogo': 1, 'Água': 1, 'Planta': 1, 'Elétrico': 1, 'Gelo': 1, 'Lutador': 1, 'Venenoso': 1, 'Terra': 1, 'Voador': 1, 'Psíquico': 1, 'Inseto': 1, 'Pedra': 1, 'Fantasma': 1, 'Dragão': 2, 'Noturno': 1, 'Metal': 0.5, 'Fada': 0},
                'Noturno': {'Normal': 1, 'Fogo': 1, 'Água': 1, 'Planta': 1, 'Elétrico': 1, 'Gelo': 1, 'Lutador': 0.5, 'Venenoso': 1, 'Terra': 1, 'Voador': 1, 'Psíquico': 2, 'Inseto': 1, 'Pedra': 1, 'Fantasma': 2, 'Dragão': 1, 'Noturno': 0.5, 'Metal': 1, 'Fada': 0.5},
                'Metal': {'Normal': 1, 'Fogo': 0.5, 'Água': 0.5, 'Planta': 1, 'Elétrico': 0.5, 'Gelo': 2, 'Lutador': 1, 'Venenoso': 1, 'Terra': 1, 'Voador': 1, 'Psíquico': 1, 'Inseto': 1, 'Pedra': 2, 'Fantasma': 1, 'Dragão': 1, 'Noturno': 1, 'Metal': 0.5, 'Fada': 2},
                'Fada': {'Normal': 1, 'Fogo': 0.5, 'Água': 1, 'Planta': 1, 'Elétrico': 1, 'Gelo': 1, 'Lutador': 2, 'Venenoso': 0.5, 'Terra': 1, 'Voador': 1, 'Psíquico': 1, 'Inseto': 1, 'Pedra': 1, 'Fantasma': 1, 'Dragão': 2, 'Noturno': 2, 'Metal': 0.5, 'Fada': 1}
    }
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