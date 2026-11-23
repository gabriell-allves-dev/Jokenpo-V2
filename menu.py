def menu():
    green = '\033[1;32m'

    print(f'{green}='*6 + 'JOKENPÔ - v2' + '='*6)

    print('\n[1] - J1 VS COM')
    print('[2] - J1 VS J2')
    print('[3] - Sair')

    opcao = int(input('\nAlternativa: '))
    return opcao