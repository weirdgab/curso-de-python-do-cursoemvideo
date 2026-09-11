print('\033[31;43mOlá, Mundo!\n')  # Letra vermelha com fundo amarelo

# Letra vermelha em negrito com fundo amarelo
print('\033[1;31;43mOlá, Mundo!\n')

# Tirando formatações no final da linha
print('\033[1;31;43mOlá, Mundo!\n\033[m')

# Letra branca fundo mangenta e texto sublinhado.
print('\033[4;30;45mOlá, Mundo!\033[m')

# Letra preta com fundo branco (inversão)
print('\033[7;30mOlá, Mundo!\033[m')

# Letra Azul com fundo amarelo (inversão)
print('\033[7;33;44mOlá, Mundo!\033[m')


# Mudando cor de variáveis específicas
a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a, b))

# Forma de print organizado
nome = 'Gabriel'
print('Olá! Muito prazer em te conhecer, {}{}{}'.format(
    '\033[4;34m', nome, '\033[m'))

# Organização versão 2
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7;30m'}

nome = 'Gabriel'
print('Olá! Muito prazer em te conhecer, {}{}{}'.format(
    cores['pretoebranco'], nome, cores['limpa']))
