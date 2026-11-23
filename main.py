from menu import menu
from jogar_vs_com import j1_vs_com
from jogar_vs_jogador import j1_vs_j2
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
    j1_vs_j2()

# Encerrar execução
elif opcao == 3:
    print(f'{red}AVISO: EM PRODUÇÃO!{green}') 
