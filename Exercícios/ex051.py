print('=' * 20)
print('10 Termos de uma PA')
print('=' * 20)

primeiroTermo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

for c in range(1, 10):
    print(primeiroTermo, '-> ', end='')
    primeiroTermo += razao

print('ACABOU', '\n')
