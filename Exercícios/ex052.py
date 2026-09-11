numero = int(input('Digite um número inteiro: '))
divisor = 0
contador = 0

for c in range(1, numero + 1):
    divisor += 1
    if numero % divisor == 0:
        contador += 1
        print('\033[33m{}\033[m'.format(c), end=' ')
    else:
        print('\033[31m{}\033[m'.format(c), end=' ')

print('\n')
print('O número foi divido {} vezes.'.format(contador))
if contador == 2:
    print('Por tanto ele é primo!')
else:
    print('Por tanto ele não é primo!')
