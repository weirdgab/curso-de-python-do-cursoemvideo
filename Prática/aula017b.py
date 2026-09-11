# FUNÇÕES COM LISTAS
valores = []
valores.append(1)
valores.append(2)
valores.append(3)

# Remoção com tratamento de erro para valor não encontrado.
if 5 in valores:
    valores.remove(5)
else:
    print('Não encontrei o número 5.')

# Alternativa de impressão de lista.
for v in valores:
    print(f'{v}...')

# Numerando índices
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')

# Lendo valores pelo teclado e adicionando a lista.
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
print('Cheguei ao final da lista.')

# Python conecta listas ao adicionar uma a outra.
a = [2, 3, 4, 7]
b = a
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')

# Fazendo cópia de listas.
c = a[:]
c[2] = 4

print(f'Lista A: {a}')
print(f'Lista C: {c}')
