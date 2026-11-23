import random

print('='*6 + 'JOKENPÔ - v2' + '='*6)

print('\n[1] - J1 VS COM')
print('[2] - J1 VS J2')
print('[3] - Sair')

opcao = int(input('\nAlternativa: '))

# Jogador 1 VS Computador
while True:
    if opcao == 1:

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
                print('Valor inválido!')
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

        elif (escolha_J1 == 1 and escolha_com == 3) or \
            (escolha_J1 == 2 and escolha_com == 1) or \
            (escolha_J1 == 3 and escolha_com == 2):
            
            print('\nVOCÊ VENCEU!')

        else:
            print('\nVOCÊ PERDEU!')



        print('\n[1] - jogar novamente')
        print('[2] - Sair')

        opcao = int(input('\nAlternativa: '))

        if opcao == 1:
            continue

        else:
            break

        

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
                    print('\nValor inválido!')

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
                    print('\nValor inválido!')

            if escolha_J1 == escolha_J2:
                print('\nEMPATE!')

            elif (escolha_J1 == 1 and escolha_com == 3) or \
                (escolha_J1 == 2 and escolha_com == 1) or \
                (escolha_J1 == 3 and escolha_com == 2):
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
        print('AVISO: EM PRODUÇÃO!') 
        break