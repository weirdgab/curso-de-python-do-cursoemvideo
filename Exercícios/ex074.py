import random

numeros = (random.randint(1, 10), random.randint(1, 10),
           random.randint(1, 10), random.randint(1, 10))
print(f'Lista de números: {numeros}')

maiorNumero = 0
menorNumero = 0

for numero in numeros:
    if numero > maiorNumero:
        maiorNumero = numero
    if menorNumero == 0:
        menorNumero = numero
    elif numero < menorNumero:
        menorNumero = numero

print(f'O maior número da lista foi: {maiorNumero}')
print(f'O menor número foi {menorNumero}')
