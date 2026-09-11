jogador = {}

jogador['nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas o {jogador["nome"]} jogou?: '))
jogador['total'] = 0
gols = []

for c in range(0, partidas):
    gols.append(int(
        input(f'    Quantos gols na {c + 1}° partida? ')))
    jogador['total'] += gols[c]

jogador['gols'] = gols

print('-=' * 30)
print(jogador)
print('-=' * 30)

for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')

print('-=' * 30)
print(f'O jogador {jogador['nome']} jogou {partidas} partidas.')

for c in range(0, partidas):
    print(f'    => Na partida {c + 1}, fez {gols[c]} gols.')
print(f'Fez um total de {jogador['total']} gols.')
