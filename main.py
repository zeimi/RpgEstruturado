import os
import time
from classes import Pokemon

def main():
    time_pokemon = choose_pokemon()
    menuPrincipal(time_pokemon)

# ---------------------------------
# Variáveis do sistema:

def choose_pokemon():    
    lista = []
    qnt=3
    while qnt!=0:
        os.system('cls||clear')
        print(f'Escolha {qnt} Pokémon')
        print("1. Meowth")
        print("2. Machamp")
        print("3. Pidgeot")
        print("4. Weezing")
        print("5. Dugtrio")
        print("6. Golem")
        print("7. Butterfree")
        print("8. Gengar")
        print("9. Steelix")
        print("10. Venusaur")
        print("11. Charizard")
        print("12. Blastoise")
        print("13. Pikachu")
        print("14. Alakazam")
        print("15. Lapras")
        print("16. Dragonite")
        print("17. Umbreon")
        print("18. Jigglypuff")
        player_pokemon = int(input("Digite o número do seu Pokémon: "))
        
        if player_pokemon == 1:
            player_pokemon1 = Pokemon("Meowth", 15, 90, "Normal")
            lista.append(player_pokemon1)
            qnt-=1
            
        elif player_pokemon == 2:
            player_pokemon2 = Pokemon("Machamp", 20, 110, "Lutador")
            lista.append(player_pokemon2)
            qnt-=1
        
        elif player_pokemon == 3:
            player_pokemon3 = Pokemon("Pidgeot", 15, 100, "Voador")
            lista.append(player_pokemon3)
            qnt-=1

        elif player_pokemon == 4:
            player_pokemon3 = Pokemon("Weezing", 5, 130, "Venenoso")
            lista.append(player_pokemon3)
            qnt-=1

        elif player_pokemon == 5:
            player_pokemon3 = Pokemon("Dugtrio", 15, 110, "Terra")
            lista.append(player_pokemon3)
            qnt-=1

        elif player_pokemon == 6:
            player_pokemon3 = Pokemon("Golem", 15, 120, "Pedra")
            lista.append(player_pokemon3)
            qnt-=1

        elif player_pokemon == 7:
            player_pokemon3 = Pokemon("Butterfree", 10, 80, "Inseto")
            lista.append(player_pokemon3)
            qnt-=1

        elif player_pokemon == 8:
            player_pokemon3 = Pokemon("Gengar", 25, 90, "Fantasma")
            lista.append(player_pokemon3)
            qnt-=1

        elif player_pokemon == 9:
            player_pokemon3 = Pokemon("Steelix", 10, 130, "Metal")
            lista.append(player_pokemon3)
            qnt-=1

        elif player_pokemon == 10:
            player_pokemon3 = Pokemon("Venusaur", 10, 120, "Planta")
            lista.append(player_pokemon3)
            qnt-=1

        elif player_pokemon == 11:
            player_pokemon3 = Pokemon("Charizard", 20, 100, "Fogo")
            lista.append(player_pokemon3)
            qnt-=1

        elif player_pokemon == 12:
            player_pokemon3 = Pokemon("Blastoise", 15, 110, "Água")
            lista.append(player_pokemon3)
            qnt-=1

        elif player_pokemon == 13:
            player_pokemon3 = Pokemon("Pikachu", 25, 80, "Elétrico")
            lista.append(player_pokemon3)
            qnt-=1

        elif player_pokemon == 14:
            player_pokemon3 = Pokemon("Alakazam", 25, 90, "Psíquico")
            lista.append(player_pokemon3)
            qnt-=1

        elif player_pokemon == 15:
            player_pokemon3 = Pokemon("Lapras", 20, 120, "Gelo")
            lista.append(player_pokemon3)
            qnt-=1

        elif player_pokemon == 16:
            player_pokemon3 = Pokemon("Dragonite", 30, 100, "Dragão")
            lista.append(player_pokemon3)
            qnt-=1

        elif player_pokemon == 17:
            player_pokemon3 = Pokemon("Umbreon", 20, 90, "Noturno")
            lista.append(player_pokemon3)
            qnt-=1

        elif player_pokemon == 18:
            player_pokemon3 = Pokemon("Jigglypuff", 20, 80, "Fada")
            lista.append(player_pokemon3)
            qnt-=1

        else:
            print("Pokémon Inválido.")
            choose_pokemon()
    return lista


def inventario():
    print('nada')

def menuPrincipal(time_pokemon):
    os.system('cls||clear')
    print('Olá. Bem vindo ao jogo.')
    nome = input('Qual é o seu nome? -> ')
    os.system('cls||clear')
    escolha = int(input(
    f"""
    -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    O que deseja, {nome}?
    Escolha uma das funções abaixo!
    -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    1 - Ir a loja
    2 - Habilidades
    3 - Adversários
    4 - Sair
    -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    Equipe atual: 
    1) {time_pokemon[0].pokemon}
    2) {time_pokemon[1].pokemon}
    3) {time_pokemon[2].pokemon}
    """
    ))
    match escolha:
        case 1:
            os.system('cls||clear')
            print('Escolheu Ir as compras.')
            time.sleep(1)
            print('.')
            time.sleep(1)
            print('..')
            time.sleep(1)
            print('...')
            time.sleep(1)
            os.system('cls||clear')
        case 2:
            os.system('cls||clear')
            print('Escolheu Habilidades.')
            input('Aperte qualquer coisa para continuar:')
        case 3:
            os.system('cls||clear')
            print('Escolheu Adversários.')
            input('Aperte qualquer coisa para continuar:')
        case 4:
            os.system('cls||clear')
            print('Escolheu Sair.')
            input('Aperte qualquer coisa para continuar:')

def equipamento():
    print('nada')



main()