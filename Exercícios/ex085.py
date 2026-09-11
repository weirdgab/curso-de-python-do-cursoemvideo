numeros = []
pares = []
impares = []
dados = []

for c in range(0, 7):
    dados.append(int(input(f'Digite o {c + 1}° número da lista: ')))
    if dados[0] % 2 == 0:
        pares.append(dados[0])
    else:
        impares.append(dados[0])
    dados.clear()

numeros.append(pares)
numeros.append(impares)
numeros.sort()

print(f'Os valores ímpares digitados foram: {impares}')
print(f'Os valores pares digitados foram: {pares}')
