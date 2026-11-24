def j1_vs_j2():
    green = '\033[1;32m'
    red = '\033[1;31m'
    import time
    import pwinput

    time.sleep(0.5)
    jogador_1 = input('\nNome do jogador 1: ').upper()
    time.sleep(0.5)
    jogador_2 = input('\nNome do jogador 2: ').upper()
        
    while True:
        time.sleep(0.5)
        print('Espere um pouco...')
        time.sleep(1)
        print('\n' + '='*6 + 'Escolha do jogador 1' + '='*6)

        print('\n[1] - Pedra')
        time.sleep(0.5)
        print('[2] - Papel')
        time.sleep(0.5)
        print('[3] - Tesoura')
        time.sleep(0.5)

        opcao_J1 = int(pwinput.pwinput('\nAlternativa: ', mask = '*'))
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
            print(f'\n{red}Valor inválido!{green}')

    while True:
        time.sleep(1)
        print('\n' + '='*6 + 'Escolha do jogador 2' + '='*6)
        
        time.sleep(0.5)
        print('\n[1] - Pedra')
        time.sleep(0.5)
        print('[2] - Papel')
        time.sleep(0.5)
        print('[3] - Tesoura')
        time.sleep(0.5)

        opcao_J2 = int(pwinput.pwinput('\nAlternativa: ', mask = '*'))

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
        time.sleep(0.5)
        print(f'{jogador_1} escolheu: {escolha_J1}')
        time.sleep(0.5)
        print(f'{jogador_2} escolheu: {escolha_J2}')
        time.sleep(0.5)
        print('\nEMPATE!')

    elif (escolha_J1 == 'Pedra' and escolha_J2 == 'Tesoura') or \
        (escolha_J1 == 'Papel' and escolha_J2 == 'Pedra') or \
        (escolha_J1 == 'Tesoura' and escolha_J2 == 'Papel'):
        time.sleep(0.5)
        print(f'{jogador_1} escolheu: {escolha_J1}')
        time.sleep(0.5)
        print(f'{jogador_2} escolheu: {escolha_J2}')
        time.sleep(0.5)
        print(f'\n{jogador_1} GANHOU!')

    else:
        time.sleep(0.5)
        print(f'{jogador_1} escolheu: {escolha_J1}')
        print(f'{jogador_2} escolheu: {escolha_J2}')
        time.sleep(0.5)
        print(f'\n{jogador_2} GANHOU!')
    
    time.sleep(0.5)
    print('\n[1] - Jogar novamente')
    time.sleep(0.5)
    print('[2] - Sair')
    time.sleep(0.3)

    opcao = int(input('\nAlternativa: '))
    return opcao