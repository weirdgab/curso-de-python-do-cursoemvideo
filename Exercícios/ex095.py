jogador = dict()
time = list()
partidas = list()
cod = 0

while True:
    jogador['nome'] = str(input('Nome do Jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(0, tot):
        partidas.append(int(input(f'    Quantos gols na partida {c + 1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    partidas.clear()
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'nN':
        break

print('-=' * 30)
print(f'cod {"nome":<20}{"gols":<20}{"total":<20}')

print('-' * 30)
for i, j in enumerate(time):
    print(f'{i:>3} {j['nome']:<20}{str(j["gols"]):<20}{j['total']:<20}')
print('-' * 30)

while True:
    cod = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if cod == 999:
        break
    while cod < 0 or cod > len(time):
        print(f'ERRO! Não existe jogador com o código {cod}!')
        cod = int(input('Mostrar dados de qual jogador? (999 para parar) '))
        if cod == 999:
            break
    if cod == 999:
        break
    print(f' -- LEVANTAMENTO DO JOGADOR {time[cod]['nome']}:')
    for c in range(0, len(time[cod]['gols'])):
        print(f' -- No jogo {c + 1} fez {time[cod]['gols'][c]} gols.')
    print('-' * 30)

print('<< VOLTE SEMPRE >>')
