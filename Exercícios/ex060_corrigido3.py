n = int(input('Digite um número inteiro par calcular seu fatorial: '))
c = n
f = 1

for i in range(1, n + 1):
    f *= c
    c -= 1

print('O fatorial de {} é {}.'.format(n, f))
