from functions import menu, j1_vs_com, j1_vs_j2
import time
import sys

green = '\033[1;32m'
red = '\033[1;31m'

while True:

    # Menu
    opcao = menu()

    # Jogador 1 VS Computador
    if opcao == 1:
        while True:
            opcao = j1_vs_com()

            if opcao == 1:
                continue

            elif opcao == 2:
                break

    # Jogador 1 VS Jogador 2
    elif opcao == 2:
        while True:
            opcao = j1_vs_j2()

            if opcao == 1:
                continue

            elif opcao == 2:
                break

    # Encerrar execução
    elif opcao == 3:
        time.sleep(1.5)
        print(f'\n{red}Finalizando execução...{green}')
        time.sleep(2.5)
        print(f'\n{red}Finalizado!{green}')
        time.sleep(1.5)
        sys.exit()

    else:
        print(f'{red}Valor inválido!{green}')