from time import sleep
from random import randint

print('-=' * 30)
print(' ' * 15, 'PALPITES DA MEGA SENA')
print('-=' * 30)

numeros = []
dados = []
verificacao = 'S'
numJogos = 0

while verificacao not in 'nN':
    numJogos = int(input('Quantos jogos serão sorteados? '))
    for c in range(0, numJogos):
        for v in range(0, 6):
            dados.append(randint(1, 60))
        numeros.append(dados[:])
        dados.clear()
        print(f'Jogo {c + 1}: {numeros[0]}')
        sleep(1)
        numeros.clear()
    verificacao = str(input('Deseja continuar? [S/n]: '))

print('-=' * 30)
print('Programa encerrado...')
