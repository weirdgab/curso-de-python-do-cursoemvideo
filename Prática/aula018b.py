# Acessando valores na lista de listas
galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]

# Primeiro índice seleciona a lista dentro da matriz
print(galera[2])

# Segundo índice seleciona o valor dessa lista
print(galera[2][1])

# Imprimindo de forma sequencial cada lista da matriz
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')
