print('=' * 20, '\n10 Termos de uma PA:')
print('=' * 20)

primeiroTermo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
cont = 0

while cont != 10:
    print(primeiroTermo, end=' ')
    primeiroTermo += razao
    cont += 1

print('Fim da PA!')
