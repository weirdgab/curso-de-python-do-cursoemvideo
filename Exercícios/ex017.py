print('Resultado com pow():\n')

catetoOposto = float(input('Digite o valor do cateto oposto: '))
catetoAdjacente = float(input('Digite o valor do cateto adjacente: '))
quadradoHipotenusa = pow(catetoOposto, 2) + pow(catetoAdjacente, 2)
resultado = pow(quadradoHipotenusa, 1/2)

print('O valor da hipotenusa é: {}\n'.format(resultado))

print('Resultado com **:\n')

catetoOposto2 = float(input('Digite o valor do cateto oposto: '))
catetoAdjacente2 = float(input('Digite o valor do cateto adjacente: '))
quadradoHipotenusa2 = (catetoOposto**2) + (catetoAdjacente**2)
resultado2 = quadradoHipotenusa2**(1/2)

print('O valor da hipotenusa é: {}'.format(resultado2))
