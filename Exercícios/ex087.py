matriz = []
matriz1 = []
matriz2 = []
matriz3 = []
somaPares = 0
somaTerceiraColuna = 0
maiorValorSegundaLinha = 0

for c in range(0, 3):
    matriz1.append(int(input(f'Digite um valor para [0, {c}]: ')))
    if matriz1[-1] % 2 == 0:
        somaPares += matriz1[-1]
    if c == 2:
        somaTerceiraColuna += matriz1[2]

for c in range(0, 3):
    matriz2.append(int(input(f'Digite um valor para [1, {c}]: ')))
    if matriz2[-1] % 2 == 0:
        somaPares += matriz2[-1]
    if c == 2:
        somaTerceiraColuna += matriz2[2]
    if c == 0:
        maiorValorSegundaLinha = matriz2[0]
    elif maiorValorSegundaLinha < matriz2[-1]:
        maiorValorSegundaLinha = matriz2[-1]

for c in range(0, 3):
    matriz3.append(int(input(f'Digite um valor para [2, {c}]: ')))
    if matriz3[-1] % 2 == 0:
        somaPares += matriz3[-1]
    if c == 2:
        somaTerceiraColuna += matriz3[2]

matriz.append(matriz1)
matriz.append(matriz2)
matriz.append(matriz3)

print('-=' * 30)
print(f'[ {matriz[0][0]} ] [ {matriz[0][1]} ] [ {matriz[0][2]} ]\n[ {matriz[1][0]} ] [ {matriz[1][1]} ] [ {matriz[1][2]} ]\n[ {matriz[2][0]} ] [ {matriz[2][1]} ] [ {matriz[2][2]} ]')
print('-=' * 30)

print(
    f'A soma de todos os valores pares da matriz é igual a {somaPares}')
print(f'A soma dos valores da terceira coluna é igual a {somaTerceiraColuna}')
print(f'O maior valor da segunda linha foi {maiorValorSegundaLinha}')
