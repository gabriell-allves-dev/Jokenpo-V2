def j1_vs_com():
    import random
    green = '\033[1;32m'
    red = '\033[1;31m'

    while True:
        print('\n' + '='*6 + 'SUA ESCOLHA' + '='*6)

        print('\n[1] - Pedra')
        print('[2] - Papel')
        print('[3] - Tesoura')

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

    print(f'\nVocê escolheu: {escolha_J1}')
    print('\nComputador pensando...')
    print(f'\nComputador escolheu: {escolha_com}')

    if escolha_J1 == escolha_com:
        print('\nEMPATE!')

    elif (escolha_J1 == 'Pedra' and escolha_com == 'Tesoura') or \
        (escolha_J1 == 'Papel' and escolha_com == 'Pedra') or \
        (escolha_J1 == 'Tesoura' and escolha_com == 'Papel'):
        
        print('\nVOCÊ VENCEU!')

    else:
        print(f'\n{red}VOCÊ PERDEU!{green}')