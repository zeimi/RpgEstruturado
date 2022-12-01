import os
import time
from classes import Pokemon, Trainer

def main(time_lider):    
    global nome
    nome = input('Qual é o seu nome? -> ')
    time_pokemon = choose_pokemon()
    menuPrincipal(time_pokemon, time_lider)

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
            input('Aperte qualquer coisa para continuar:')
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
    1 - Brock       4 - Sabrina     7 - Voltar
    2 - Misty       5 - Giovanni
    3 - Lt. Surge   6 - Lance
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
            nome_lider = "Brock, líder do tipo Pedra"
            leader_pokemon1 = Pokemon("Onix", 10, 120, "Pedra")
            leader_pokemon2 = Pokemon("Golem", 15, 120, "Pedra")
            leader_pokemon3 = Pokemon("Rhydon", 10, 130, "Pedra")
            lider = Trainer("Brock", "Pedra", leader_pokemon1, leader_pokemon2, leader_pokemon3, "Boulder")
            lista.append(leader_pokemon1)
            lista.append(leader_pokemon2)
            lista.append(leader_pokemon3)
            time_lider = lista
            print (f"""Equipe do Brock: 
            1) Nome:{time_lider[0].pokemon}
            2) Nome:{time_lider[1].pokemon}
            3) Nome:{time_lider[2].pokemon}
            """
            )
            input('Aperte qualquer coisa para continuar:')
            batalha(time_pokemon, time_lider)
        case 2:
            os.system('cls||clear')
            nome_lider = "Misty, líder do tipo Água"
            leader_pokemon1 = Pokemon("Golduck", 15, 100, "Água")
            leader_pokemon2 = Pokemon("Starmie", 15, 110, "Água")
            leader_pokemon3 = Pokemon("Gyarados", 20, 120, "Água")
            lider = Trainer("Misty", "Água", leader_pokemon1, leader_pokemon2, leader_pokemon3, "Cascade")
            lista.append(leader_pokemon1)
            lista.append(leader_pokemon2)
            lista.append(leader_pokemon3)
            time_lider = lista
            print (f"""Equipe da Misty: 
            1) Nome:{time_lider[0].pokemon}
            2) Nome:{time_lider[1].pokemon}
            3) Nome:{time_lider[2].pokemon}
            """
            )
            input('Aperte qualquer coisa para continuar:')
            batalha(time_pokemon, time_lider)
        case 3:
            os.system('cls||clear')
            nome_lider = "Lt. Surge, líder do tipo Elétrico"
            leader_pokemon1 = Pokemon("Jolteon", 20, 100, "Elétrico")
            leader_pokemon2 = Pokemon("Magneton", 10, 110, "Elétrico")
            leader_pokemon3 = Pokemon("Raichu", 25, 90, "Elétrico")
            lider = Trainer("Lt. Surge", "Elétrico", leader_pokemon1, leader_pokemon2, leader_pokemon3, "Thunder")
            lista.append(leader_pokemon1)
            lista.append(leader_pokemon2)
            lista.append(leader_pokemon3)
            time_lider = lista
            print (f"""Equipe do Lt. Surge: 
            1) Nome:{time_lider[0].pokemon}
            2) Nome:{time_lider[1].pokemon}
            3) Nome:{time_lider[2].pokemon}
            """
            )
            input('Aperte qualquer coisa para continuar:')
            batalha(time_pokemon, time_lider)
        case 4:
            os.system('cls||clear')
            nome_lider = "Sabrina, líder do tipo Psíquico"
            leader_pokemon1 = Pokemon("Mr. Mime", 20, 100, "Psíquico")
            leader_pokemon2 = Pokemon("Hypno", 15, 110, "Psíquico")
            leader_pokemon3 = Pokemon("Alakazam", 25, 90, "Psíquico")
            lider = Trainer("Sabrina", "Psíquico", leader_pokemon1, leader_pokemon2, leader_pokemon3, "Marsh")
            lista.append(leader_pokemon1)
            lista.append(leader_pokemon2)
            lista.append(leader_pokemon3)
            time_lider = lista
            print (f"""Equipe da Sabrina: 
            1) Nome:{time_lider[0].pokemon}
            2) Nome:{time_lider[1].pokemon}
            3) Nome:{time_lider[2].pokemon}
            """
            )
            input('Aperte qualquer coisa para continuar:')
            batalha(time_pokemon, time_lider)
        case 5:
            os.system('cls||clear')
            nome_lider = "Giovanni, líder do tipo Terra"
            leader_pokemon1 = Pokemon("Dugtrio", 15, 110, "Terra")
            leader_pokemon2 = Pokemon("Nidoqueen", 15, 110, "Terra")
            leader_pokemon3 = Pokemon("Nidoking", 20, 120, "Terra")
            lider = Trainer("Giovanni", "Terra", leader_pokemon1, leader_pokemon2, leader_pokemon3, "Earth")
            lista.append(leader_pokemon1)
            lista.append(leader_pokemon2)
            lista.append(leader_pokemon3)
            time_lider = lista
            print (f"""Equipe do Giovanni: 
            1) Nome:{time_lider[0].pokemon}
            2) Nome:{time_lider[1].pokemon}
            3) Nome:{time_lider[2].pokemon}
            """
            )
            input('Aperte qualquer coisa para continuar:')
            batalha(time_pokemon, time_lider)
        case 6:
            os.system('cls||clear')
            nome_lider = "Lance, campeão de Kanto"
            leader_pokemon1 = Pokemon("Charizard", 20, 100, "Fogo")
            leader_pokemon2 = Pokemon("Aerodactyl", 30, 110, "Pedra")
            leader_pokemon3 = Pokemon("Dragonite", 35, 120, "Dragão")
            lider = Trainer("Lance", "Dragão", leader_pokemon1, leader_pokemon2, leader_pokemon3, "Champion")
            lista.append(leader_pokemon1)
            lista.append(leader_pokemon2)
            lista.append(leader_pokemon3)
            time_lider = lista
            print (f"""Equipe do Lance: 
            1) Nome:{time_lider[0].pokemon}
            2) Nome:{time_lider[1].pokemon}
            3) Nome:{time_lider[2].pokemon}
            """
            )
            input('Aperte qualquer coisa para continuar:')
            batalha(time_pokemon, time_lider)
        case 7:
            os.system('cls||clear')
            print('Voltar.')
            input('Aperte qualquer coisa para continuar:')
            menuPrincipal(time_pokemon, time_lider)
    return time_lider



def equipePokemon(time_pokemon, time_lider):
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
            equipePokemon(time_pokemon, time_lider)
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
            equipePokemon(time_pokemon, time_lider)
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
            equipePokemon(time_pokemon, time_lider)
        case 4:
            os.system('cls||clear')
            print('Voltar.')
            input('Aperte qualquer coisa para continuar:')
            menuPrincipal(time_pokemon, time_lider)

def menuPrincipal(time_pokemon, time_lider):
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
            adversario = adversarios(time_pokemon, time_lider)
        case 2:
            os.system('cls||clear')
            print("Escolheu Equipe.")
            input('Aperte qualquer coisa para continuar:')
            equipePokemon(time_pokemon, time_lider)
            
        case 3:
            os.system('cls||clear')
            print('Escolheu Sair.')
            input('Aperte qualquer coisa para continuar:')
            exit()

def batalha(time_pokemon, time_lider):
    os.system('cls||clear')
    print(f"""
    -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    Batalha entre {nome} e {nome_lider}
    -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    """)
    input('Aperte qualquer coisa para continuar:')
    
    while time_pokemon[0].health > 0 and time_lider[0].health > 0:
        os.system('cls||clear')
        
        print(f"""
        -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        {time_pokemon[0].pokemon} vs {time_lider[0].pokemon}
        -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        """)
        print(f"""
        -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        {time_pokemon[0].pokemon} - Vida: {time_pokemon[0].health} - Força: {time_pokemon[0].force}
        {time_lider[0].pokemon} - Vida: {time_lider[0].health} - Força: {time_lider[0].force}
        -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        """)
        escolha = int(input(
        f"""
        -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        O que deseja fazer, {nome}?
        Escolha uma das ações abaixo!
        -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        1 - Atacar
        2 - Trocar de Pokémon
        3 - Fugir
        -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        """
        ))
        match escolha:
            case 1:
                os.system('cls||clear')
                danodado = time_pokemon[0].force * Pokemon.attackDict[time_pokemon[0].type][time_lider[0].type]
                danorecebido = time_lider[0].force * Pokemon.attackDict[time_lider[0].type][time_pokemon[0].type]
                print('Escolheu Atacar.')
                input('Aperte qualquer coisa para continuar:')
                print(f"{time_pokemon[0].pokemon} utilizou seu ataque do tipo {time_pokemon[0].type}!\n")
                time_lider[0].health -= danodado
                print(f"\n{time_lider[0].pokemon} perdeu {danodado} de vida!\n")
                input('Aperte qualquer coisa para continuar:')
                os.system('cls||clear')
                print(f"{time_lider[0].pokemon} utilizou seu ataque do tipo {time_lider[0].type}!\n")
                time_pokemon[0].health -= danorecebido
                print(f"\n{time_pokemon[0].pokemon} perdeu {danorecebido} de vida!\n")
                input('Aperte qualquer coisa para continuar:')
            case 2:
                os.system('cls||clear')
                print('Escolheu Trocar de Pokémon.')
                input('Aperte qualquer coisa para continuar:')
                trocarPokemon(time_pokemon, time_lider)
            case 3:
                os.system('cls||clear')
                print('Escolheu Fugir.')
                input('Aperte qualquer coisa para continuar:')
                menuPrincipal(time_pokemon, time_lider)

    if time_pokemon[0].health <= 0 and time_pokemon[1].health <= 0 and time_pokemon[2].health <= 0:
        os.system('cls||clear')
        print(f"""
        -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
            Você perdeu a batalha.
        -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        """)
        time_pokemon[0].health = time_pokemon[0].maxhealth
        time_pokemon[1].health = time_pokemon[1].maxhealth
        time_pokemon[2].health = time_pokemon[2].maxhealth
        time_lider[0].health = time_lider[0].maxhealth
        time_lider[1].health = time_lider[1].maxhealth
        time_lider[2].health = time_lider[2].maxhealth
        if nome_lider == 'Brock, líder do tipo Pedra':
            print(f"""
                                    Brock venceu!
            -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-
            Brock: Você batalhou bem. Mas a minha defesa de Pedra é invencível!
            """)
            input('Aperte qualquer coisa para continuar:')
        elif nome_lider == 'Misty, líder do tipo Água':
            print(f"""
                            Misty venceu!
            -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=
            Misty: Viu? Essa é a força dos Pokémon de Água!
            """)
            input('Aperte qualquer coisa para continuar:')
        elif nome_lider == 'Lt. Surge, líder do tipo Elétrico':
            print(f"""
                                         Lt. Surge venceu!
            -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=
            Lt. Surge: É isso aí! Quando o assunto é Pokémon Elétrico, eu sou o número 1!
            """)
            input('Aperte qualquer coisa para continuar:')
        elif nome_lider == 'Sabrina, líder do tipo Psíquico':
            print(f"""
                                Sabrina venceu!
            -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=
            Sabrina: Essa vitória... foi exatamente como eu previ.
            """)
            input('Aperte qualquer coisa para continuar:')
        elif nome_lider == 'Giovanni, líder do tipo Terra':
            print(f"""
                             Giovanni venceu!
            -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-
            Giovanni: Eu espero que nos encontremos novamente...
            """)
            input('Aperte qualquer coisa para continuar:')
        elif nome_lider == 'Lance, campeão de Kanto':
            print(f"""
                                    Lance venceu!
            -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
            Lance: Eu nunca desisto. Meus dragões são criaturas lendárias!
            """)
            input('Aperte qualquer coisa para continuar:')
        menuPrincipal(time_pokemon, time_lider)

    elif time_lider[0].health <= 0 and time_lider[1].health <= 0 and time_lider[2].health <= 0:
        os.system('cls||clear')
        print(f"""
        -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
            Você venceu a batalha!
        -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        """)
        time_pokemon[0].health = time_pokemon[0].maxhealth
        time_pokemon[1].health = time_pokemon[1].maxhealth
        time_pokemon[2].health = time_pokemon[2].maxhealth
        time_lider[0].health = time_lider[0].maxhealth
        time_lider[1].health = time_lider[1].maxhealth
        time_lider[2].health = time_lider[2].maxhealth
        if nome_lider == 'Brock, líder do tipo Pedra':
            print(f"""
                     Você venceu o Brock!
            -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=
            Brock: Eu te subestimei. Você é um treinador muito bom. 
                    Aqui está a insígnia da Rocha!
            """)
            input('Aperte qualquer coisa para continuar:')
        elif nome_lider == 'Misty, líder do tipo Água':
            print(f"""
                        Você venceu a Misty!
            -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-
            Misty: Uau! você é muito forte! Parabéns!
            Pode ficar com essa insígia da Cascata!
            """)
            input('Aperte qualquer coisa para continuar:')
        elif nome_lider == 'Lt. Surge, líder do tipo Elétrico':
            print(f"""
                    Você venceu o Lt. Surge!
            -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-
            Lt. Surge: Nossa! você é pra valer, moleque!
            Tudo bem, tome essa insígnia do Trovão!
            """)
            input('Aperte qualquer coisa para continuar:')
        elif nome_lider == 'Sabrina, líder do tipo Psíquico':
            print(f"""
                            Você venceu a Sabrina!
            -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=
            Sabrina: Eu estou chocada! Mas uma derrota é uma derrota.
                    Você merece a insígnia do Espírito!
            """)
            input('Aperte qualquer coisa para continuar:')
        elif nome_lider == 'Giovanni, líder do tipo Terra':
            print(f"""
                            Você venceu o Giovanni!
            -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=
            Giovanni: Ha! Essa foi uma batalha intensa! Você venceu!
                Como prova, aqui está a insíquia da Terra!
            """)
            input('Aperte qualquer coisa para continuar:')
        elif nome_lider == 'Lance, campeão de Kanto':
            print(f"""
                                         Você venceu o Lance!
            -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=
            Lance: É isso! Não queria admitir, mas você é o melhor treinador que eu já vi!
                                    Você agora é o campeão de Kanto!
            """)
            input('Aperte qualquer coisa para continuar:')
            menuPrincipal(time_pokemon, time_lider)
        input('Aperte qualquer coisa para continuar:')
        menuPrincipal(time_pokemon, time_lider)

    # Quando o pokémon morrer, troca para o seguinte
    elif time_pokemon[0].health <= 0:
        time_pokemon[0], time_pokemon[1], time_pokemon[2] = time_pokemon[1], time_pokemon[2], time_pokemon[0]
        batalha(time_pokemon, time_lider)
    elif time_lider[0].health <= 0:
        time_lider[0], time_lider[1], time_lider[2] = time_lider[1], time_lider[2], time_lider[0]
        batalha(time_pokemon, time_lider)


def trocarPokemon(time_pokemon, time_lider):
    os.system('cls||clear')
    print(f"""
    -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
          Trocar de Pokémon
    -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    """)
    escolha = int(input(
    f"""
    -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    Escolha um dos seus pokémons para trocar.
    -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    1) {time_pokemon[0].pokemon}
    2) {time_pokemon[1].pokemon}
    3) {time_pokemon[2].pokemon}
    -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    """))
    match escolha:
        case 1:
            os.system('cls||clear')
            print(f"""
            -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
            {time_pokemon[0].pokemon} já está em batalha!
            -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
            """)
            input('Aperte qualquer coisa para continuar:')
        case 2:
            os.system('cls||clear')
            if time_pokemon[1].health <= 0:
                print(f"""
                -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
                {time_pokemon[1].pokemon} está desmaiado!
                -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
                """)
                input('Aperte qualquer coisa para continuar:')
            else:
                print(f"""
                -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
                Você escolheu {time_pokemon[1].pokemon}
                -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
                """)
                input('Aperte qualquer coisa para continuar:')
                time_pokemon[0], time_pokemon[1] = time_pokemon[1], time_pokemon[0]
                time_pokemon[0].health -= time_lider[0].force
        case 3:
            if time_pokemon[2].health <= 0:
                os.system('cls||clear')
                print(f"""
                -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
                {time_pokemon[2].pokemon} está desmaiado!
                -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
                """)
                input('Aperte qualquer coisa para continuar:')
            else:
                os.system('cls||clear')
                print(f"""
                -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
                Você escolheu {time_pokemon[2].pokemon}
                -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
                """)
                input('Aperte qualquer coisa para continuar:')
                time_pokemon[0], time_pokemon[2] = time_pokemon[2], time_pokemon[0]
                time_pokemon[0].health -= time_lider[0].force

main(time_lider=adversarios)