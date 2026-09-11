numeros = (int(input('Digite um número: ')), int(input('Digite outro número: ')), int(input(
    'Digite mais um número: ')), int(input('Digite o último número: ')))

qtdDeNoves = 0
numerosPares = 'Nenhum número digitado foi par'
posicaoNumeroTres = -1

for numero in numeros:
    if numero == 9:
        qtdDeNoves += 1
    if numero % 2 == 0:
        if numerosPares == 'Nenhum número digitado foi par':
            numerosPares = f'{numero}'
        else:
            numerosPares += f', {numero}'
    if numero == 3:
        posicaoNumeroTres = numeros.index(3)

print(f'Foram digitados {qtdDeNoves} número(s) nove digitados.')
print(f'O número 3 apareceu na posição {posicaoNumeroTres}.')
print(f'Os números pares digitados foram: {numerosPares}')
