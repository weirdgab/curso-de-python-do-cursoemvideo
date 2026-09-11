numeros = []
numero = -1
for c in range(1, 6):
    if numero == -1:
        numero = int(input('teste: '))
        numeros.append(numero)
        print('Adicionado na posição 0 da lista...')
    else:
        numero = int(input('teste: '))
        if numero >= numeros[-1]:
            numeros.append(numero)
            print('Adicionado ao final da lista...')
        elif len(numeros) < 2:
            numeros.insert(0, numero)
            print('Adicionado na posição 0 da lista...')
        elif len(numeros) < 3:
            if numero < numeros[-2]:
                numeros.insert(-2, numero)
                print('Adicionado na posição 0 da lista...')
            else:
                numeros.insert(-1, numero)
                print('Adicionado ao final da lista...')
        elif len(numeros) < 4:
            if numero < numeros[-3]:
                numeros.insert(-3, numero)
                print('Adicionado na posição 0 da lista...')
            elif numero < numeros[-2]:
                numeros.insert(-2, numero)
                print('Adicionado na posição 1 da lista...')
        elif len(numeros) < 5:
            if numero < numeros[-4]:
                numeros.insert(-4, numero)
                print('Adicionado na posição 0 da lista...')
            elif numero < numeros[-3]:
                numeros.insert(-3, numero)
                print('Adicionado na posição 1 da lista...')
            elif numero < numeros[-2]:
                numeros.insert(-2, numero)
                print('Adicionado na posição 2 da lista...')
        elif len(numeros) < 6:
            if numero < numeros[-5]:
                numeros.insert(-5, numero)
                print('Adicionado na posição 0 da lista...')
            elif numero < numeros[-4]:
                numeros.insert(-4, numero)
                print('Adicionado na posição 1 da lista...')
            elif numero < numeros[-3]:
                numeros.insert(-3, numero)
                print('Adicionado na posição 2 da lista...')
            elif numero < numeros[-2]:
                numeros.insert(-2, numero)
                print('Adicionado na posição 3 da lista...')

print(f'A lista ordenada é {numeros}')
