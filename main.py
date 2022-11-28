import os
import time
from classes import Pokemon

def main():
    print('Função Principal.')
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
        print("1. Bulbasaur")
        print("2. Charmander")
        print("3. Squirtle")
        player_pokemon = int(input("Enter the number of your Pokémon: "))
        
        if player_pokemon == 1:
            player_pokemon1 = Pokemon("Bulbasaur", 100, 100, "Grass")
            lista.append(player_pokemon1)
            qnt-=1
            
        elif player_pokemon == 2:
            player_pokemon2 = Pokemon("Charmander", 100, 100, "Grass")
            lista.append(player_pokemon2)
            qnt-=1
        
        elif player_pokemon == 3:
            player_pokemon3 = Pokemon("Squirtle", 100, 100, "Water")
            lista.append(player_pokemon3)
            qnt-=1

        else:
            print("Invalid Pokemon")
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