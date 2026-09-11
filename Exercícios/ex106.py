from time import sleep

while True:
    print('\033[0;30;42m~\033[m' * 30)
    print('\033[0;30;42m    SISTEMA DE AJUDA PyHELP')
    print('\033[0;30;42m~\033[m' * 30)
    resp = input('Função ou Biblioteca > ').strip().lower()
    if resp == 'fim':
        print('\033[0;30;41m~\033[m' * 30)
        print('\033[0;30;41m          ATÉ LOGO!')
        print('\033[0;30;41m~\033[m' * 30)
        break
    while resp.isnumeric():
        print('ERRO! Digite uma função válida!')
        resp = input('Função ou Biblioteca > ')
    print('\033[0;30;46m~\033[m' * 40)
    print(f'\033[0;30;46m   Acessando o manual do comando "{resp}"')
    print('\033[0;30;46m~\033[m' * 40)
    sleep(1)
    help(resp)
    sleep(1)
