import os
import time

def main():
    print('Função Principal.')
    menuPrincipal()

# ---------------------------------
# Variáveis do sistema:



def inventario():
    print('nada')

def menuPrincipal():
    os.system('cls||clear')
    escolha = int(input(
    """
    -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    Menu principal
    Escolha uma das funções abaixo!
    -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    1 - Ir a loja
    2 - Habilidades
    3 - Adversários
    4 - Sair
    -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
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