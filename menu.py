def menu():
    green = '\033[1;32m'
    import time

    print(f'{green}='*6 + 'JOKENPÔ - v2' + '='*6)
    time.sleep(1.5)

    print('\n[1] - J1 VS COM')
    time.sleep(0.5)
    print('[2] - J1 VS J2')
    time.sleep(0.5)
    print('[3] - Sair')
    time.sleep(0.5)
    
    opcao = int(input('\nAlternativa: '))
    return opcao