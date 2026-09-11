lista = []
listaMenor = -1
listaMaior = -1
indiceMenor = -1
indiceMaior = -1
indice = -1

for cont in range(0, 5):
    lista.append(int(input('Adicione um valor: ')))
    indice += 1
    if listaMaior == -1:
        listaMaior = lista[-1:]
        indiceMaior = indice
    elif lista[-1:] > listaMaior:
        listaMaior = lista[-1:]
        indiceMaior = indice
    if listaMenor == -1:
        listaMenor = lista[-1:]
        indiceMenor = indice
    elif listaMenor > lista[-1:]:
        listaMenor = lista[-1:]
        indiceMenor = indice


print(f'A lista digitada foi {lista}.')
print(
    f'O maior número foi {listaMaior} com o índice {indiceMaior}.')
print(f'O menor número foi {listaMenor} com o índice {indiceMenor}.')
