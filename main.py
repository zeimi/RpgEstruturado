import os
import time
from classes import Pokemon

def main():    
    global nome
    nome = input('Qual é o seu nome? -> ')
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
        print("""
        1. Meowth       7. Butterfree       13. Pikachu
        2. Machamp      8. Gengar           14. Alakazam
        3. Pidgeot      9. Steelix          15. Lapras
        4. Weezing      10. Venusaur        16. Dragonite
        5. Dugtrio      11. Charizard       17. Umbreon
        6. Golem        12. Blastoise       18. Jigglypuff
        """)
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
            input('Aperte qualquer coisa para continuar:')
    return lista


def adversarios(time_pokemon):
    os.system('cls||clear')
    escolha = int(input(
    f"""
    -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
                     {nome}, Escolha seu adversário:
    -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    1 - Brock
    2 - Misty
    3 - Lt. Surge
    4 - Voltar
    -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    Equipe atual: 
    1) Nome:{time_pokemon[0].pokemon}
    2) Nome:{time_pokemon[1].pokemon}
    3) Nome:{time_pokemon[2].pokemon} 
    -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    """
    ))
    match escolha:
        case 1:
            os.system('cls||clear')
            print('Função de enfrentar o Brock ainda não foi implementada.')
            input('Aperte qualquer coisa para continuar:')
            adversarios(time_pokemon)
        case 2:
            os.system('cls||clear')
            print('Função de enfrentar a misty ainda não foi implementada.')
            input('Aperte qualquer coisa para continuar:')
            adversarios(time_pokemon)
        case 3:
            os.system('cls||clear')
            print('Função de enfrentar o lt. surge ainda não foi implementada.')
            input('Aperte qualquer coisa para continuar:')
            adversarios(time_pokemon)
        case 4:
            os.system('cls||clear')
            print('Voltar.')
            input('Aperte qualquer coisa para continuar:')
            menuPrincipal(time_pokemon)



def equipePokemon(time_pokemon):
    os.system('cls||clear')
    escolha = int(input(
    f"""
    -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
                     {nome}, como deseja organizar
                             a sua equipe?
    -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    1 - Organizar por força
    2 - Organizar por nome
    3 - Organizar por Vida (Bubble sort)
    4 - Voltar
    -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    Equipe atual: 
    1) Nome:{time_pokemon[0].pokemon}   Força:{time_pokemon[0].force}   Vida:{time_pokemon[0].health}   Tipo:{time_pokemon[0].type}
    2) Nome:{time_pokemon[1].pokemon}   Força:{time_pokemon[1].force}   Vida:{time_pokemon[1].health}   Tipo:{time_pokemon[1].type}
    3) Nome:{time_pokemon[2].pokemon}   Força:{time_pokemon[2].force}   Vida:{time_pokemon[2].health}   Tipo:{time_pokemon[2].type}
    -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    """
    ))
    match escolha:
        case 1:
            os.system('cls||clear')
            print('Organizar por força.')
            sorteio_forca = input('Deseja organizar por força de forma aleatória? (S/N)')
            if sorteio_forca == 'S' or sorteio_forca == 's':
                time_pokemon.sort(key=lambda x: x.force, reverse=True)
                print('Organização por força realizada com sucesso.')
            else:
                print('Organização por força cancelada.')
            input('Aperte qualquer coisa para continuar:')
            equipePokemon(time_pokemon)
        case 2:
            os.system('cls||clear')
            print('Organizar por nome.')
            sorteio_nome = input("Deseja organizar por ordem alfabética? (S/N) ")
            if sorteio_nome == "S" or sorteio_nome == "s":
                time_pokemon.sort(key=lambda x: x.pokemon)
                print("Organizado por ordem alfabética.")
            else:
                print("Organização cancelada.")
            input('Aperte qualquer coisa para continuar:')
            equipePokemon(time_pokemon)
        case 3:
            os.system('cls||clear')
            print('Organizar por Vida (Bubble sort).')
            sorteio_bubble = input("Deseja organizar a equipe por vida no estilo bubble sorte? (S/N) ")
            if sorteio_bubble == "S" or sorteio_bubble == "s":
                for i in range(len(time_pokemon)):
                    for j in range(len(time_pokemon)-1):
                        if time_pokemon[j].health > time_pokemon[j+1].health:
                            time_pokemon[j], time_pokemon[j+1] = time_pokemon[j+1], time_pokemon[j]
                print("Organização realizada com sucesso.")
            else:
                print("Organização cancelada.")
            input('Aperte qualquer coisa para continuar:')
            equipePokemon(time_pokemon)
        case 4:
            os.system('cls||clear')
            print('Voltar.')
            input('Aperte qualquer coisa para continuar:')
            menuPrincipal(time_pokemon)

def menuPrincipal(time_pokemon):
    os.system('cls||clear')
    print('Olá. Bem vindo ao jogo.')
    os.system('cls||clear')
    escolha = int(input(
    f"""
    -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    O que deseja, {nome}?
    Escolha uma das funções abaixo!
    -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    1 - Adversários
    2 - Equipe
    3 - Sair
    -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    Equipe atual: 
    1) {time_pokemon[0].pokemon}
    2) {time_pokemon[1].pokemon}
    3) {time_pokemon[2].pokemon}
    -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    """
    ))
    match escolha:
        case 1:
            os.system('cls||clear')
            print('Escolheu Adversários.')
            input('Aperte qualquer coisa para continuar:')
            adversarios(time_pokemon)
        case 2:
            os.system('cls||clear')
            print("Escolheu Equipe.")
            input('Aperte qualquer coisa para continuar:')
            equipePokemon(time_pokemon)
            
        case 3:
            os.system('cls||clear')
            print('Escolheu Sair.')
            input('Aperte qualquer coisa para continuar:')


main()