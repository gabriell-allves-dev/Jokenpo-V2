def caixa():
    print('='*30)
    return None

def menu():
    green = '\033[1;32m'
    import time
    print(f'{green}')
    
    caixa()
    print('='*6 + 'JOKENPÔ - v2' + '='*6)
    caixa()
    time.sleep(1.5)

    print()

    caixa()
    print('[1] - J1 VS COM')
    time.sleep(0.5)
    print('[2] - J1 VS J2')
    time.sleep(0.5)
    print('[3] - Sair')
    time.sleep(0.5)
    caixa()

    print()

    caixa()
    opcao = int(input('Alternativa: '))
    caixa()
    return opcao

def j1_vs_com():
    import random
    import time
    green = '\033[1;32m'
    red = '\033[1;31m'

    while True:
        time.sleep(1)
        print()

        caixa()
        print('='*6 + 'SUA ESCOLHA' + '='*6)
        caixa()

        print()

        caixa()
        time.sleep(0.5)
        print('[1] - Pedra')
        time.sleep(0.5)
        print('[2] - Papel')
        time.sleep(0.5)
        print('[3] - Tesoura')
        caixa()
        time.sleep(0.5)

        print()
        
        caixa()        
        opcao = int(input('\nAlternativa: '))
        caixa()

        if opcao == 1:
            escolha_J1 = 'Pedra'
            break

        elif opcao == 2:
            escolha_J1 = 'Papel'
            break

        elif opcao == 3:
            escolha_J1 = 'Tesoura'
            break

        else:
            print(f'{red}Valor inválido!{green}')
            continue

    computador = random.randint(1,3)

    if computador == 1:
        escolha_com = 'Pedra'

    elif computador == 2:
        escolha_com = 'Papel'

    else:
        escolha_com = 'Tesoura'

    time.sleep(0.5)
    caixa()
    print(f'Você escolheu: {escolha_J1}')
    caixa()
    time.sleep(1)
    print()
    caixa()
    print('Computador pensando...')
    time.sleep(1.5)
    print(f'\nComputador escolheu: {escolha_com}')
    time.sleep(0.5)
    print(f'Você escolheu: {escolha_J1}')
    caixa()
    time.sleep(1)
    print()

    if escolha_J1 == escolha_com:
        caixa()
        print('EMPATE!')
        caixa()

    elif (escolha_J1 == 'Pedra' and escolha_com == 'Tesoura') or \
        (escolha_J1 == 'Papel' and escolha_com == 'Pedra') or \
        (escolha_J1 == 'Tesoura' and escolha_com == 'Papel'):
        caixa()
        print('VOCÊ VENCEU!')
        caixa()

    else:
        caixa()
        print(f'{red}VOCÊ PERDEU!{green}')
        caixa()

    time.sleep(1.5)
    print()
    caixa()
    print('[1] - Jogar novamente')
    time.sleep(0.5)
    print('[2] - Sair')
    caixa()
    time.sleep(0.5)

    print()
    
    caixa()
    opcao = int(input('\nAlternativa: '))
    caixa()
    return opcao

def j1_vs_j2():
    green = '\033[1;32m'
    red = '\033[1;31m'
    import time
    import pwinput

    time.sleep(0.5)
    caixa()
    jogador_1 = input('Nome do jogador 1: ').upper()
    time.sleep(0.5)
    jogador_2 = input('\nNome do jogador 2: ').upper()
    caixa()
    print()
        
    while True:
        time.sleep(0.5)
        caixa()
        print('Espere um pouco...')
        caixa()
        time.sleep(1)
        print()

        caixa()
        print('='*6 + 'Escolha do jogador 1' + '='*6)

        print()

        caixa()
        print('[1] - Pedra')
        time.sleep(0.5)
        print('[2] - Papel')
        time.sleep(0.5)
        print('[3] - Tesoura')
        caixa()
        time.sleep(0.5)

        print()

        caixa()
        opcao_J1 = int(pwinput.pwinput('\nAlternativa: ', mask = '*'))
        caixa()
        time.sleep(0.3)

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
            print(f'\n{red}Valor inválido!{green}\n')

    while True:
        time.sleep(1)
        print()
        caixa()
        print('\n' + '='*6 + 'Escolha do jogador 2' + '='*6)
        caixa()
        
        print()

        time.sleep(0.5)
        caixa()
        print('[1] - Pedra')
        time.sleep(0.5)
        print('[2] - Papel')
        time.sleep(0.5)
        print('[3] - Tesoura')
        caixa()
        time.sleep(0.5)

        print()
        
        caixa()
        opcao_J2 = int(pwinput.pwinput('Alternativa: ', mask = '*'))
        caixa()

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
            print(f'\n{red}Valor inválido!{green}\n')

    if escolha_J1 == escolha_J2:
        print()
        time.sleep(0.5)
        caixa()
        print(f'{jogador_1} escolheu: {escolha_J1}')
        caixa()
        print()
        time.sleep(0.5)
        caixa()
        print(f'{jogador_2} escolheu: {escolha_J2}')
        caixa()
        time.sleep(0.5)
        print('\nEMPATE!')

    elif (escolha_J1 == 'Pedra' and escolha_J2 == 'Tesoura') or \
        (escolha_J1 == 'Papel' and escolha_J2 == 'Pedra') or \
        (escolha_J1 == 'Tesoura' and escolha_J2 == 'Papel'):
        print()
        time.sleep(0.5)
        caixa()
        print(f'{jogador_1} escolheu: {escolha_J1}')
        caixa()
        print()
        time.sleep(0.5)
        caixa()
        print(f'{jogador_2} escolheu: {escolha_J2}')
        caixa()
        time.sleep(0.5)
        print(f'\n{jogador_1} GANHOU!')
    else:
        print()
        time.sleep(0.5)
        caixa()
        print(f'{jogador_1} escolheu: {escolha_J1}')
        caixa()
        print()
        time.sleep(0.5)
        caixa()
        print(f'{jogador_2} escolheu: {escolha_J2}')
        caixa()
        time.sleep(0.5)
        print(f'\n{jogador_2} GANHOU!')
    
    time.sleep(0.5)
    print()
    caixa()
    print('[1] - Jogar novamente')
    time.sleep(0.5)
    print('[2] - Sair')
    caixa()
    time.sleep(0.3)
    print()
    
    caixa()
    opcao = int(input('Alternativa: '))
    caixa()    
    return opcao