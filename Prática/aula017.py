# Declarando lista
num = [2, 5, 9, 1]

# Substituindo elementos
num[2] = 3

# Adicionando elementos
num.append(7)
num.insert(2, 0)  # Adicionando valor 0 na posição 2

# Organizando elementos
num.sort()
num.sort(reverse=True)  # Organizando elementos de trás para frente

# Verificando números de elementos
print(f'Essa lista tem {len(num)} elementos.')

# Removendo elementos
num.pop()  # Removendo o último elemento
num.pop(5)  # Removendo o elemento 5

# "remove" deleta o primeiro número pedido da esquerda para a direita.
num.remove(2)
