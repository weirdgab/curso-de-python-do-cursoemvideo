from random import randint
from time import sleep


def sorteia(num):
    print('Soreando 5 valores da lista: ', end='')
    for c in range(0, 5):
        num.append(randint(1, 10))
        print(f'{num[c]} ', end='', flush=True)
        sleep(0.5)
    print('PRONTO!')


def somaPar(num):
    soma = 0
    for v in num:
        if v % 2 == 0:
            soma += v
    print(f'Somando os valores {num}, temos {soma}')


numeros = []
sorteia(numeros)
somaPar(numeros)
