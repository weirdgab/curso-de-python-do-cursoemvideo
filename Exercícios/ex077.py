palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis',
            'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')

cont = 0
for palavra in palavras:
    if cont == 0:
        print(f'Na palavra {palavra} temos: ', end='')
    else:
        print(f'\nNa palavra {palavra} temos: ', end='')
    if 'a' in palavra:
        print('a ', end='')
    if 'e' in palavra:
        print('e ', end='')
    if 'i' in palavra:
        print('i ', end='')
    if 'o' in palavra:
        print('o ', end='')
    if 'u' in palavra:
        print('u ', end='')
    cont += 1
print('\n')
