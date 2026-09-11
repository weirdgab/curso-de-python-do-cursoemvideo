# Modificando strings:
frase = '   Curso em Vídeo Python   '
print(frase, '\n')

# String em maiúsculas:
print(frase.upper(), '\n')

# String em minúsculas:
print(frase.lower(), '\n')

# Removendo espaços extras da string:
print(frase.strip(), '\n')

# Substituindo conjunto de caracteres da frase:
print(frase.replace('Python', 'Android'), '\n')

# Transformando cada palavra em frase em um elemento de lista
print(frase.split(), '\n')

# Convertendo frase para lista:
dividido = frase.split()
print(frase, '\n')

# Exibindo posição 0 da da frase transformada em lista
print(dividido[0], '\n')

# Exibindo a posição 3 do segundo elemento da lista
print(dividido[2][3], '\n')
