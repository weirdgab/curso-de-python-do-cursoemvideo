soma = 0
quantidadeMúltiplos = 0
for c in range(1, 501):
    if c % 3 == 0 and c % 2 != 0:
        soma += c
        quantidadeMúltiplos += 1

print('A soma de todos os {} valores requisitados são {}.'.format(quantidadeMúltiplos, soma))
