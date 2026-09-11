from time import sleep


def maior(* num):
    maior = 0
    print('-=' * 30)
    print('Analisando valores passados', end='')
    for c in range(0, 4):
        sleep(0.5)
        print('.', end='', flush=True)
    print()
    print(f'Foram informados {len(num)} valor(es) ao todo.')
    if len(num) != 0:
        for i in range(0, len(num)):
            print(f'{num[i]} ', end='', flush=True)
            sleep(0.5)
            if i == 0:
                maior = num[0]
            elif num[i] > maior:
                maior = num[i]
        print(f'O maior valor informado foi {maior}')
    else:
        print('O maior valor informado não existe.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
