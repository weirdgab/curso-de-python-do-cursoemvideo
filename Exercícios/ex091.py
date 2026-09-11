from random import randint
from time import sleep

print('Valores sorteados:')

jogos = {'jogador1': randint(1, 6), 'jogador2': randint(
    1, 6), 'jogador3': randint(1, 6), 'jogador4': randint(1, 6)}

resultados = []
jogadores = []

for k, v in jogos.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
    if len(resultados) == 0 or v < resultados[-1]:
        resultados.append(v)
        jogadores.append(k)
    else:
        pos = 0
        while pos < len(resultados):
            if v >= resultados[pos]:
                resultados.insert(pos, v)
                jogadores.insert(pos, k)
                break
            pos += 1

print('-=' * 30)
print(' ' * 10, 'RAKING DOS JOGADORES')

for c in range(0, 4):
    print(f'{c + 1}° Lugar - {jogadores[c]} com {resultados[c]} pontos.')
    sleep(1)
