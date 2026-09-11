n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
n3 = float(input('Digite o terceiro valor: '))

# Verificando quem é maior:
if n1 > n2 and n1 > n3:
    print('O maior valor entre os três é {}.'.format(n1))
elif n2 > n1 and n2 > n3:
    print('O maior valor entre os três é {}'.format(n2))
elif n3 > n1 and n3 > n2:
    print('O maior valor entre os três é {}'.format(n3))
elif n1 == n2 and n1 == n3:
    print('Todos os valores são iguais!')

# Verificando quem é menor:
if n1 < n2 and n1 < n3:
    print('O menor valor entre os três é {}.'.format(n1))
elif n2 < n1 and n2 < n3:
    print('O menor valor entre os três é {}'.format(n2))
elif n3 < n1 and n3 < n2:
    print('O menor valor entre os três é {}'.format(n3))
