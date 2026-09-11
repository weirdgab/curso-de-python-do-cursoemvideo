# Analisando strings
frase = 'Curso em Vídeo Python'
print(frase, '\n')

# Quantas letras "o" minúsculo existem na frase:
print(frase.count('o'), '\n')

# Quantas letras "O" maiúsculo existem na frase
print(frase.count('O'), '\n')

# Quantas letras "O" maiúsculo existem na frase após ela ser convertida inteiramente para letras maiúsculas
print(frase.upper().count('O'), '\n')

# Quantos caracteres há na frase
print(len(frase), '\n')

# Verificando conjunto de caracteres na frase
print('Curso' in frase, '\n')

# Frase alterada com espaços extras:
frase = '   Curso em Vídeo Python   '
print(frase, '\n')

# Quantos caracteres há na frase com espaços extras
print(len(frase), '\n')

# Tamanho da frase após remover espaços extras do meio e final da frase:
print(len(frase.strip()), '\n')

# Procurando "Curso" na frase
print(frase.find('Curso'), '\n')

# Procurando "video" na frase
print(frase.find('video'), '\n')

# Procurando "video" na frase após converter todos os caracteres para minúsculos
print(frase.lower().find('video'), '\n')

# MÉTODO FIND É CASE SENSITIVE!!
