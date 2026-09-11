n = int(input('Digite um número: '))

print('O número digitado foi {}. \nO dobro de {} vale {}. \nO triplo de {} vale {}. \nA raíz quadrada de {} vale aproximadamente {:.2f}.'.format(
    n, n, (n*2), n, (n*3), n, pow(n, (1/2))))
