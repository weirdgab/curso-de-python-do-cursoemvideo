soma = 0

for c in range(1, 7):
    valor = int(input('Digite um valor inteiro: '))
    if valor % 2 == 0:
        soma += valor

print('A soma de todos os valores inteiros digitados é igual a {}.'.format(soma))
