def área(l, c):
    a = l * c
    print(f'A área de um terreno {l:.1f}x{c:.2f} é de {a:.1f}m².')


print(' Controle de Terrenos')
print('-' * 30)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
área(l, c)
