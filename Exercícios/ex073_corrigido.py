times = ('Palmeiras', 'Flamengo', 'Fluminense', 'São Paulo', 'Athletico-PR', 'Bahia', 'Bragantino', 'Coritiba', 'Vitória', 'Botafogo',
         'Atlético-MG', 'Internacional', 'Vasco', 'Grêmio', 'Cruzeiro', 'Santos', 'Corinthians', 'Mirassol', 'Remo', 'Chapecoense')

print(20 * '=')
print(f'Lista de times do Brasileirão: {times}')
print(20 * '=')
print(f'Os 5 primeiros colocados são: {times[0:5]}')
print(20 * '=')
print(f'A lista de times de forma ordenada fica: {sorted(times)}')
print(20 * '=')
print(f'Os 4 últimos são: {times[-4:]}')
print(20 * '=')
print(f'O Chapecoense está na posição: {times.index('Chapecoense') + 1}')
print(20 * '=')
