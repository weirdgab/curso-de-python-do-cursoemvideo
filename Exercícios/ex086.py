matriz = []
matriz1 = []
matriz2 = []
matriz3 = []

for c in range(0, 3):
    matriz1.append(int(input(f'Digite um valor para [0, {c}]: ')))

for c in range(0, 3):
    matriz2.append(int(input(f'Digite um valor para [1, {c}]: ')))

for c in range(0, 3):
    matriz3.append(int(input(f'Digite um valor para [2, {c}]: ')))

matriz.append(matriz1)
matriz.append(matriz2)
matriz.append(matriz3)

print('-=' * 30)
print(f'[ {matriz[0][0]} ] [ {matriz[0][1]} ] [ {matriz[0][2]} ]\n[ {matriz[1][0]} ] [ {matriz[1][1]} ] [ {matriz[1][2]} ]\n[ {matriz[2][0]} ] [ {matriz[2][1]} ] [ {matriz[2][2]} ]')
