def j1_vs_com():
    import random
    import time
    green = '\033[1;32m'
    red = '\033[1;31m'

    while True:
        time.sleep(1)
        print('\n' + '='*6 + 'SUA ESCOLHA' + '='*6)

        time.sleep(0.5)
        print('\n[1] - Pedra')
        time.sleep(0.5)
        print('[2] - Papel')
        time.sleep(0.5)
        print('[3] - Tesoura')
        time.sleep(0.5)

        opcao = int(input('\nAlternativa: '))

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
    print(f'\nVocê escolheu: {escolha_J1}')
    time.sleep(1)
    print('\nComputador pensando...')
    time.sleep(1.5)
    print(f'\nComputador escolheu: {escolha_com}')
    time.sleep(0.5)
    print(f'Você escolheu: {escolha_J1}')
    time.sleep(1)

    if escolha_J1 == escolha_com:
        print('\nEMPATE!')

    elif (escolha_J1 == 'Pedra' and escolha_com == 'Tesoura') or \
        (escolha_J1 == 'Papel' and escolha_com == 'Pedra') or \
        (escolha_J1 == 'Tesoura' and escolha_com == 'Papel'):
        
        print('\nVOCÊ VENCEU!')

    else:
        print(f'\n{red}VOCÊ PERDEU!{green}')

    time.sleep(1.5)
    print('\n[1] - Jogar novamente')
    time.sleep(0.5)
    print('[2] - Sair')
    time.sleep(0.5)
    
    opcao = int(input('\nAlternativa: '))
    return opcao