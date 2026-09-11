n = 0
cont = 0
maior = 0
menor = 0
soma = 0
condicaoParada = 's'

while condicaoParada in 'sS':
    n = float(input('Digite um número: '))
    cont += 1
    if cont == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    soma += n
    condicaoParada = input('Quer continuar? [S/N]: ')
media = soma / cont
print('Você digitou {} números.'.format(cont))
print('O maior número foi {} e o menor número foi {}.'.format(maior, menor))
print('A média entre eles foi de {:.2f}'.format(media))
