largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = largura * altura
litro = area / 2

print('Sua parede tem a dimensão de {}x{} e sua área é de {:.3f}m².'.format(
    largura, altura, area))
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(litro))
