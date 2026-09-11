# Contador infinito com comando break
soma = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break  # Comando de parada
    soma += n

# Formatação com fstrings
print(f'A soma dos números digitados é {soma}.')
