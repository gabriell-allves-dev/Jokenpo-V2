from menu import menu
from jogar_vs_com import j1_vs_com
import random
import time

green = '\033[1;32m'
red = '\033[1;31m'

# Menu
opcao = menu()

# Jogador 1 VS Computador
if opcao == 1:
    j1_vs_com()

# Jogador 1 VS Jogador 2
elif opcao == 2:
    jogador_1 = input('\nNome do jogador 1: ').upper()
    jogador_2 = input('\nNome do jogador 2: ').upper()
    
    while True:
        while True:
            print('\n' + '='*6 + 'Escolha do jogador 1' + '='*6)

            print('\n[1] - Pedra')
            print('[2] - Papel')
            print('[3] - Tesoura')

            opcao_J1 = int(input('\nAlternativa: '))

            if opcao_J1 == 1:
                escolha_J1 = 'Pedra'
                break

            elif opcao_J1 == 2:
                escolha_J1 = 'Papel'
                break

            elif opcao_J1 == 3:
                escolha_J1 = 'Tesoura'
                break

            else:
                print(f'\n{red}Valor inválido!{green}')

        while True:
            print('\n' + '='*6 + 'Escolha do jogador 2' + '='*6)
            
            print('\n[1] - Pedra')
            print('[2] - Papel')
            print('[3] - Tesoura')

            opcao_J2 = int(input('\nAlternativa: '))

            if opcao_J2 == 1:
                escolha_J2 = 'Pedra'
                break

            elif opcao_J2 == 2:
                escolha_J2 = 'Papel'
                break

            elif opcao_J2 == 3:
                escolha_J2 = 'Tesoura'
                break

            else:
                print(f'\n{red}Valor inválido!{green}')

        if escolha_J1 == escolha_J2:
            print('\nEMPATE!')

        elif (escolha_J1 == 'Pedra' and escolha_J2 == 'Tesoura') or \
            (escolha_J1 == 'Papel' and escolha_J2 == 'Pedra') or \
            (escolha_J1 == 'Tesoura' and escolha_J2 == 'Papel'):
            print(f'\n{jogador_1} GANHOU!')

        else:
            print(f'\n{jogador_2} GANHOU!')

        print('\n[1] - Jogar novamente')
        print('[2] - Sair')

        opcao = int(input('\nAlternativa: '))

        if opcao == 1:
            continue

        elif opcao == 2:
            break
            


# Encerrar execução
elif opcao == 3:
    print(f'{red}AVISO: EM PRODUÇÃO!{green}') 
