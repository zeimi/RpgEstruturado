import os
import time
from classes import Pokemon, Trainer

def main(time_lider):    
    global nome
    nome = input("""
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
                Bem vindo ao mundo de Pokémon!
                Qual é o seu nome? -> """)
    os.system('cls||clear')
    input (f"""
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
                                Olá, {nome}!
    Você é um treinador Pokémon e seu objetivo é se tornar o melhor treinador do mundo!
            Aperte qualquer coisa para escolher seu pokémon logo em seguida.
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=""")
    time_pokemon = choose_pokemon()
    menuPrincipal(time_pokemon, time_lider)

# ---------------------------------
# Variáveis do sistema:

def choose_pokemon():    
    lista = []
    qnt=3
    while qnt!=0:
        os.system('cls||clear')
        print(f"""
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        Escolha {qnt} Pokémon para formar a sua equipe:
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    1. Meowth       7. Butterfree       13. Pikachu
    2. Machamp      8. Gengar           14. Alakazam
    3. Pidgeot      9. Steelix          15. Lapras
    4. Weezing      10. Venusaur        16. Dragonite
    5. Dugtrio      11. Charizard       17. Umbreon
    6. Golem        12. Blastoise       18. Jigglypuff
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-""")
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
            player_pokemon3 = Pokemon("Dragonite", 30, 110, "Dragão")
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
            input('Aperte qualquer coisa para escolher novamente:')
    return lista


def adversarios(time_pokemon, time_lider):
    global nome_lider
    lista = []
    os.system('cls||clear')
    escolha = int(input(
    f"""
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
                {nome}, Escolha seu adversário:
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    1 - Brock       4 - Sabrina     7 - Pescador Danilo
    2 - Misty       5 - Giovanni    8 - Manoel Gomes
    3 - Lt. Surge   6 - Lance       9 - Voltar
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Equipe atual: 
1) Nome:{time_pokemon[0].pokemon}
2) Nome:{time_pokemon[1].pokemon}
3) Nome:{time_pokemon[2].pokemon} 
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Escolha:"""))
    match escolha:
        case 1:
            os.system('cls||clear')
            nome_lider = "Brock, líder do tipo Pedra"
            leader_pokemon1 = Pokemon("Onix", 10, 120, "Pedra")
            leader_pokemon2 = Pokemon("Golem", 15, 120, "Pedra")
            leader_pokemon3 = Pokemon("Rhydon", 10, 130, "Pedra")
            lider = Trainer("Brock", "Pedra", leader_pokemon1, leader_pokemon2, leader_pokemon3, "Rocha")
            lista.append(leader_pokemon1)
            lista.append(leader_pokemon2)
            lista.append(leader_pokemon3)
            time_lider = lista
            print (f"""Equipe do Brock: 
1) Nome:{time_lider[0].pokemon}
2) Nome:{time_lider[1].pokemon}
3) Nome:{time_lider[2].pokemon}""")
            input('Aperte qualquer coisa para proceder:')
            batalha(time_pokemon, time_lider)
        case 2:
            os.system('cls||clear')
            nome_lider = "Misty, líder do tipo Água"
            leader_pokemon1 = Pokemon("Golduck", 15, 100, "Água")
            leader_pokemon2 = Pokemon("Starmie", 15, 110, "Água")
            leader_pokemon3 = Pokemon("Gyarados", 20, 120, "Água")
            lider = Trainer("Misty", "Água", leader_pokemon1, leader_pokemon2, leader_pokemon3, "Cascata")
            lista.append(leader_pokemon1)
            lista.append(leader_pokemon2)
            lista.append(leader_pokemon3)
            time_lider = lista
            print (f"""Equipe da Misty: 
1) Nome:{time_lider[0].pokemon}
2) Nome:{time_lider[1].pokemon}
3) Nome:{time_lider[2].pokemon}""")
            input('Aperte qualquer coisa para proceder:')
            batalha(time_pokemon, time_lider)
        case 3:
            os.system('cls||clear')
            nome_lider = "Lt. Surge, líder do tipo Elétrico"
            leader_pokemon1 = Pokemon("Jolteon", 20, 100, "Elétrico")
            leader_pokemon2 = Pokemon("Magneton", 10, 110, "Elétrico")
            leader_pokemon3 = Pokemon("Raichu", 25, 90, "Elétrico")
            lider = Trainer("Lt. Surge", "Elétrico", leader_pokemon1, leader_pokemon2, leader_pokemon3, "Trovão")
            lista.append(leader_pokemon1)
            lista.append(leader_pokemon2)
            lista.append(leader_pokemon3)
            time_lider = lista
            print (f"""Equipe do Lt. Surge: 
1) Nome:{time_lider[0].pokemon}
2) Nome:{time_lider[1].pokemon}
3) Nome:{time_lider[2].pokemon}""")
            input('Aperte qualquer coisa para proceder:')
            batalha(time_pokemon, time_lider)
        case 4:
            os.system('cls||clear')
            nome_lider = "Sabrina, líder do tipo Psíquico"
            leader_pokemon1 = Pokemon("Mr. Mime", 20, 100, "Psíquico")
            leader_pokemon2 = Pokemon("Hypno", 15, 110, "Psíquico")
            leader_pokemon3 = Pokemon("Alakazam", 25, 90, "Psíquico")
            lider = Trainer("Sabrina", "Psíquico", leader_pokemon1, leader_pokemon2, leader_pokemon3, "Espírito")
            lista.append(leader_pokemon1)
            lista.append(leader_pokemon2)
            lista.append(leader_pokemon3)
            time_lider = lista
            print (f"""Equipe da Sabrina: 
1) Nome:{time_lider[0].pokemon}
2) Nome:{time_lider[1].pokemon}
3) Nome:{time_lider[2].pokemon}""")
            input('Aperte qualquer coisa para proceder:')
            batalha(time_pokemon, time_lider)
        case 5:
            os.system('cls||clear')
            nome_lider = "Giovanni, líder do tipo Terra"
            leader_pokemon1 = Pokemon("Dugtrio", 15, 110, "Terra")
            leader_pokemon2 = Pokemon("Nidoqueen", 15, 110, "Terra")
            leader_pokemon3 = Pokemon("Nidoking", 20, 120, "Terra")
            lider = Trainer("Giovanni", "Terra", leader_pokemon1, leader_pokemon2, leader_pokemon3, "Terra")
            lista.append(leader_pokemon1)
            lista.append(leader_pokemon2)
            lista.append(leader_pokemon3)
            time_lider = lista
            print (f"""Equipe do Giovanni: 
1) Nome:{time_lider[0].pokemon}
2) Nome:{time_lider[1].pokemon}
3) Nome:{time_lider[2].pokemon}""")
            input('Aperte qualquer coisa para proceder:')
            batalha(time_pokemon, time_lider)
        case 6:
            os.system('cls||clear')
            nome_lider = "Lance, campeão de Kanto"
            leader_pokemon1 = Pokemon("Charizard", 20, 100, "Fogo")
            leader_pokemon2 = Pokemon("Aerodactyl", 30, 110, "Voador")
            leader_pokemon3 = Pokemon("Dragonite", 35, 120, "Dragão")
            lider = Trainer("Lance", "Dragão", leader_pokemon1, leader_pokemon2, leader_pokemon3, "Campeão")
            lista.append(leader_pokemon1)
            lista.append(leader_pokemon2)
            lista.append(leader_pokemon3)
            time_lider = lista
            print (f"""Equipe do Lance: 
1) Nome:{time_lider[0].pokemon}
2) Nome:{time_lider[1].pokemon}
3) Nome:{time_lider[2].pokemon}""")
            input('Aperte qualquer coisa para proceder:')
            batalha(time_pokemon, time_lider)
        case 7:
            os.system('cls||clear')
            nome_lider = "Pescador Danilo"
            leader_pokemon1 = Pokemon("Magikarp", 5, 10, "Água")
            leader_pokemon2 = Pokemon("Magikarp", 5, 10, "Água")
            leader_pokemon3 = Pokemon("Magikarp", 5, 10, "Água")
            lider = Trainer("Pescador Danilo", "Poggers", leader_pokemon1, leader_pokemon2, leader_pokemon3, "Froggers")
            lista.append(leader_pokemon1)
            lista.append(leader_pokemon2)
            lista.append(leader_pokemon3)
            time_lider = lista
            print (f"""Equipe de Danilo: 
1) Nome:{time_lider[0].pokemon}
2) Nome:{time_lider[1].pokemon}
3) Nome:{time_lider[2].pokemon}""")
            input('Aperte qualquer coisa para proceder:')
            batalha(time_pokemon, time_lider)
        case 8:
            os.system('cls||clear')
            nome_lider = "Manoel Gomes, o homem da Caneta Azul"
            leader_pokemon1 = Pokemon("Dialga", 35, 150, "Dragão")
            leader_pokemon2 = Pokemon("Palkia", 35, 150, "Dragão")
            leader_pokemon3 = Pokemon("Arceus", 50, 200, "Divino")
            lider = Trainer("Manoel Gomes", "Divino", leader_pokemon1, leader_pokemon2, leader_pokemon3, "Caneta")
            lista.append(leader_pokemon1)
            lista.append(leader_pokemon2)
            lista.append(leader_pokemon3)
            time_lider = lista
            print (f"""Equipe do Caneta Azul: 
1) Nome:{time_lider[0].pokemon}
2) Nome:{time_lider[1].pokemon}
3) Nome:{time_lider[2].pokemon}""")
            input('Aperte qualquer coisa para proceder:')
            batalha(time_pokemon, time_lider)
        case 9:
            os.system('cls||clear')
            print('Voltar.')
            input('Aperte qualquer coisa para voltar ao menu principal:')
            menuPrincipal(time_pokemon, time_lider)
    return time_lider



def equipePokemon(time_pokemon, time_lider):
    os.system('cls||clear')
    escolha = int(input(f"""
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
Escolha:"""))
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
            input('Aperte qualquer coisa para voltar ao menu de organização:')
            equipePokemon(time_pokemon, time_lider)
        case 2:
            os.system('cls||clear')
            print('Organizar por nome.')
            sorteio_nome = input("Deseja organizar por ordem alfabética? (S/N) ")
            if sorteio_nome == "S" or sorteio_nome == "s":
                time_pokemon.sort(key=lambda x: x.pokemon)
                print("Organização por nome realizada com sucesso.")
            else:
                print("Organização por nome cancelada.")
            input('Aperte qualquer coisa para voltar ao menu de organização:')
            equipePokemon(time_pokemon, time_lider)
        case 3:
            os.system('cls||clear')
            print('Organizar por Vida (Bubble sort).')
            sorteio_bubble = input("Deseja organizar a equipe por vida no estilo bubble sort? (S/N) ")
            if sorteio_bubble == "S" or sorteio_bubble == "s":
                for i in range(len(time_pokemon)):
                    for j in range(len(time_pokemon)-1):
                        if time_pokemon[j].health > time_pokemon[j+1].health:
                            time_pokemon[j], time_pokemon[j+1] = time_pokemon[j+1], time_pokemon[j]
                print("Organização por vida realizada com sucesso.")
            else:
                print("Organização por vida cancelada.")
            input('Aperte qualquer coisa para voltar ao menu de organização:')
            equipePokemon(time_pokemon, time_lider)
        case 4:
            os.system('cls||clear')
            print('Voltar.')
            input('Aperte qualquer coisa para voltar ao menu principal:')
            menuPrincipal(time_pokemon, time_lider)

def menuPrincipal(time_pokemon, time_lider):
    os.system('cls||clear')
    escolha = int(input(f"""
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        Menu principal:
{nome}, o que deseja fazer?
Escolha uma das funções abaixo!
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
1 - Adversários
2 - Equipe
3 - Regras
4 - Sair
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Equipe atual: 
1) {time_pokemon[0].pokemon}
2) {time_pokemon[1].pokemon}
3) {time_pokemon[2].pokemon}
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Escolha:"""))
    match escolha:
        case 1:
            os.system('cls||clear')
            print('Escolheu Adversários.')
            input('Aperte qualquer coisa para seguir ao menu de adversários:')
            adversario = adversarios(time_pokemon, time_lider)
        case 2:
            os.system('cls||clear')
            print("Escolheu Equipe.")
            input('Aperte qualquer coisa para seguir ao menu de equipe:')
            equipePokemon(time_pokemon, time_lider)

        case 3:
            os.system('cls||clear')
            input("""-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Regras:
1 - O jogo consiste em uma batalha entre dois times de três pokémons.
2 - Os pokémon possuem vida, força e tipo.
3 - A vida é o valor de vida do pokémon, quando chega a 0, o pokémon é derrotado.
4 - A força é o valor de ataque do pokémon, quando o pokémon ataca, ele causa dano igual a sua força.
5 - Ao trocar de pokémon, seu próximo pokémon a entrar em campo recebe o dano da rodada.
6 - O tipo é o tipo do pokémon, que pode ser fogo, água ou grama.
7 - Os pokémon tem multiplicadores de dano baseado em tipo, por exemplo:
    O pokémon do tipo água causa dano 2x maior no pokémon do tipo fogo.
8 - Se divirta e boa sorte! 
                (APERTE QUALQUER COISA PARA VOLTAR AO MENU PRINCIPAL)
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-""")
            menuPrincipal(time_pokemon, time_lider)    
        case 4:
            os.system('cls||clear')
            print('Escolheu Sair.')
            input('Aperte qualquer coisa para sair do jogo:')
            exit()

def batalha(time_pokemon, time_lider):
    os.system('cls||clear')
    if time_pokemon[2].health > 0 and time_lider[2].health > 0:
        print(f"""
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Batalha entre {nome} e {nome_lider}
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-""")
        input('Aperte qualquer coisa para iniciar a batalha:')
        
    while time_pokemon[0].health > 0 and time_lider[0].health > 0:
        os.system('cls||clear')
        
        print(f"""-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
{time_pokemon[0].pokemon} vs {time_lider[0].pokemon}""")
        print(f"""-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
{time_pokemon[0].pokemon} - Vida: {time_pokemon[0].health} - Força: {time_pokemon[0].force}
{time_lider[0].pokemon} - Vida: {time_lider[0].health} - Força: {time_lider[0].force}""")
        escolha = int(input(f"""-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
O que deseja fazer, {nome}?
Escolha uma das ações abaixo!
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
1 - Atacar
2 - Trocar de Pokémon
3 - Fugir
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Escolha: """))
        match escolha:
            case 1:
                os.system('cls||clear')
                danodado = time_pokemon[0].force * Pokemon.attackDict[time_pokemon[0].type][time_lider[0].type]
                danorecebido = time_lider[0].force * Pokemon.attackDict[time_lider[0].type][time_pokemon[0].type]
                print('Escolheu Atacar.')
                input('Aperte qualquer coisa para realizar o ataque:')
                os.system('cls||clear')
                print(f"{time_pokemon[0].pokemon} utilizou seu ataque do tipo {time_pokemon[0].type}!")
                time_lider[0].health -= danodado
                print(f"{time_lider[0].pokemon} perdeu {danodado} de vida!")
                print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=')
                print(f"{time_lider[0].pokemon} utilizou seu ataque do tipo {time_lider[0].type}!")
                time_pokemon[0].health -= danorecebido
                print(f"{time_pokemon[0].pokemon} perdeu {danorecebido} de vida!")
                print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=')
                input('Aperte qualquer coisa para voltar ao menu de batalha:')
            case 2:
                os.system('cls||clear')
                print('Escolheu Trocar de Pokémon.')
                input('Aperte qualquer coisa para voltar ao menu de batalha:')
                trocarPokemon(time_pokemon, time_lider)
            case 3:
                os.system('cls||clear')
                print('Escolheu Fugir.')
                input('Aperte qualquer coisa para voltar ao menu principal:')
                menuPrincipal(time_pokemon, time_lider)

    if time_pokemon[0].health <= 0 and time_pokemon[1].health <= 0 and time_pokemon[2].health <= 0:
        os.system('cls||clear')
        input(f"""
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        Você perdeu a batalha.
Aperte qualquer coisa para continuar...
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-""")
        time_pokemon[0].health = time_pokemon[0].maxhealth
        time_pokemon[1].health = time_pokemon[1].maxhealth
        time_pokemon[2].health = time_pokemon[2].maxhealth
        time_lider[0].health = time_lider[0].maxhealth
        time_lider[1].health = time_lider[1].maxhealth
        time_lider[2].health = time_lider[2].maxhealth
        if nome_lider == 'Brock, líder do tipo Pedra':
            os.system('cls||clear')
            print(f"""
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-
                        Brock venceu!
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-
Brock: Você batalhou bem. Mas a minha defesa de Pedra é invencível!
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-""")
            input('Aperte qualquer coisa para voltar ao menu principal:')
        elif nome_lider == 'Misty, líder do tipo Água':
            os.system('cls||clear')
            print(f"""
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-
                         Misty venceu!
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-
        Misty: Viu? Essa é a força dos Pokémon de Água!
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-""")
            input('Aperte qualquer coisa para voltar ao menu principal:')
        elif nome_lider == 'Lt. Surge, líder do tipo Elétrico':
            os.system('cls||clear')
            print(f"""
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-
                            Lt. Surge venceu!
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-
Lt. Surge: É isso aí! Quando o assunto é Pokémon Elétrico, eu sou o número 1!
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-""")
            input('Aperte qualquer coisa para voltar ao menu principal:')
        elif nome_lider == 'Sabrina, líder do tipo Psíquico':
            os.system('cls||clear')
            print(f"""
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-
                        Sabrina venceu!
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-
        Sabrina: Essa vitória... foi exatamente como eu previ.
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-""")
            input('Aperte qualquer coisa para voltar ao menu principal:')
        elif nome_lider == 'Giovanni, líder do tipo Terra':
            os.system('cls||clear')
            print(f"""
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-
                        Giovanni venceu!
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-
        Giovanni: Eu espero que nos encontremos novamente...
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-""")
            input('Aperte qualquer coisa para voltar ao menu principal:')
        elif nome_lider == 'Lance, campeão de Kanto':
            os.system('cls||clear')
            print(f"""
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-
                            Lance venceu!
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    Lance: Eu nunca desisto. Meus dragões são criaturas lendárias!
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-""")
            input('Aperte qualquer coisa para voltar ao menu principal:')
        elif nome_lider == 'Pescador Danilo':
            os.system('cls||clear')
            print(f"""
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-
                                Pescador Danilo venceu!
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Pescador Danilo: Ganhei! Agora dá licença que eu tenho que estudar o complemento de 2.
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-""")
            input('Aperte qualquer coisa para voltar ao menu principal:')
        elif nome_lider == 'Manoel Gomes, o homem da Caneta Azul':
            os.system('cls||clear')
            print(f"""
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=
                                Manoel Gomes venceu!
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-
Manoel Gomes: Caneta azul, azul caneta, caneta azul, está marcada com minha letra...
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-""")
            input('Aperte qualquer coisa para voltar ao menu principal:')
        menuPrincipal(time_pokemon, time_lider)

    elif time_lider[0].health <= 0 and time_lider[1].health <= 0 and time_lider[2].health <= 0:
        os.system('cls||clear')
        input(f"""
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        Você venceu a batalha!
Aperte qualquer coisa para continuar...
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=""")
        time_pokemon[0].health = time_pokemon[0].maxhealth
        time_pokemon[1].health = time_pokemon[1].maxhealth
        time_pokemon[2].health = time_pokemon[2].maxhealth
        time_lider[0].health = time_lider[0].maxhealth
        time_lider[1].health = time_lider[1].maxhealth
        time_lider[2].health = time_lider[2].maxhealth
        if nome_lider == 'Brock, líder do tipo Pedra':
            os.system('cls||clear')
            print(f"""
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=
                Você venceu o Brock!
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=
Brock: Eu te subestimei. Você é um treinador muito bom. 
        Aqui está a insígnia da Rocha!
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=""")
            input('Aperte qualquer coisa para voltar ao menu principal:')
        elif nome_lider == 'Misty, líder do tipo Água':
            os.system('cls||clear')
            print(f"""
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=
                Você venceu a Misty!
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=
        Misty: Uau! você é muito forte! Parabéns!
        Pode ficar com essa insígia da Cascata!
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=""")
            input('Aperte qualquer coisa para voltar ao menu principal:')
        elif nome_lider == 'Lt. Surge, líder do tipo Elétrico':
            os.system('cls||clear')
            print(f"""
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=
             Você venceu o Lt. Surge!
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=
    Lt. Surge: Nossa! você é pra valer, moleque!
        Tudo bem, tome essa insígnia do Trovão!
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=""")
            input('Aperte qualquer coisa para voltar ao menu principal:')
        elif nome_lider == 'Sabrina, líder do tipo Psíquico':
            os.system('cls||clear')
            print(f"""
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=
                Você venceu a Sabrina!
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=
Sabrina: Eu estou chocada! Mas uma derrota é uma derrota.
        Você merece a insígnia do Espírito!
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=""")
            input('Aperte qualquer coisa para voltar ao menu principal:')
        elif nome_lider == 'Giovanni, líder do tipo Terra':
            os.system('cls||clear')
            print(f"""
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=
                Você venceu o Giovanni!
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=
Giovanni: Ha! Essa foi uma batalha intensa! Você venceu!
        Como prova, aqui está a insíquia da Terra!
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=""")
            input('Aperte qualquer coisa para voltar ao menu principal:')
        elif nome_lider == 'Lance, campeão de Kanto':
            os.system('cls||clear')
            print(f"""
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
                        Você venceu o Lance!
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Lance: É isso! Não queria admitir, mas você é o melhor treinador que eu já vi!
                    Você agora é o campeão de Kanto!
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=""")
            input('Aperte qualquer coisa para voltar ao menu principal:')
            menuPrincipal(time_pokemon, time_lider)
        elif nome_lider == 'Pescador Danilo':
            os.system('cls||clear')
            print(f"""
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=
                    Você venceu do Pescador Danilo!
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Pescador Danilo: Peraí mãe, que esse Pokémon não sabe nem batalhar!
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=""")
            input('Aperte qualquer coisa para voltar ao menu principal:')
        elif nome_lider == 'Manoel Gomes, o homem da Caneta Azul':
            os.system('cls||clear')
            print(f"""
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=
            Você venceu do Manuel Gomes!
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=
            Ai... Ai... Ai... Ai... Ai...
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=""")
            input('Aperte qualquer coisa para voltar ao menu principal:')
        menuPrincipal(time_pokemon, time_lider)

    # Quando o pokémon morrer, troca para o seguinte
    elif time_pokemon[0].health <= 0:
        os.system('cls||clear')
        print('Seu Pokémon foi derrotado!')
        time_pokemon[0], time_pokemon[1], time_pokemon[2] = time_pokemon[1], time_pokemon[2], time_pokemon[0]
        input('Aperte qualquer coisa para o próximo entrar em campo:')
        batalha(time_pokemon, time_lider)
    elif time_lider[0].health <= 0:
        os.system('cls||clear')
        print('O pokémon do líder foi derrotado!')
        time_lider[0], time_lider[1], time_lider[2] = time_lider[1], time_lider[2], time_lider[0]
        input('Aperte qualquer coisa para enfrentar o próximo Pokémon:')
        batalha(time_pokemon, time_lider)


def trocarPokemon(time_pokemon, time_lider):
    os.system('cls||clear')
    print(f"""
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    Trocar de Pokémon""")
    escolha = int(input(f"""
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Escolha um dos seus pokémons para trocar.
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
1) {time_pokemon[0].pokemon}
2) {time_pokemon[1].pokemon}
3) {time_pokemon[2].pokemon}
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Escolha: """))
    match escolha:
        case 1:
            os.system('cls||clear')
            print(f"""
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
{time_pokemon[0].pokemon} já está em batalha!
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-""")
            input('Aperte qualquer coisa para voltar:')
        case 2:
            os.system('cls||clear')
            if time_pokemon[1].health <= 0:
                print(f"""
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
{time_pokemon[1].pokemon} está desmaiado!
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-""")
                input('Aperte qualquer coisa para voltar:')
            else:
                print(f"""
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Você escolheu {time_pokemon[1].pokemon}
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-""")
                input('Aperte qualquer coisa para continuar:')
                time_pokemon[0], time_pokemon[1] = time_pokemon[1], time_pokemon[0]
                time_pokemon[0].health -= time_lider[0].force
        case 3:
            if time_pokemon[2].health <= 0:
                os.system('cls||clear')
                print(f"""
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
{time_pokemon[2].pokemon} está desmaiado!
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-""")
                input('Aperte qualquer coisa para voltar:')
            else:
                os.system('cls||clear')
                print(f"""
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Você escolheu {time_pokemon[2].pokemon}
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-""")
                input('Aperte qualquer coisa para continuar:')
                time_pokemon[0], time_pokemon[2] = time_pokemon[2], time_pokemon[0]
                time_pokemon[0].health -= time_lider[0].force

main(time_lider=adversarios)