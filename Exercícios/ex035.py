print('-' * 30)
print('   Analisador de Triângulos   ')
print('-' * 30, '\n')

a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

if a + b > c and a + c > b and b + c > a:
    print('Estes segmentos podem formar um triângulo!')
else:
    print('Estes segmentos não podem formar um triângulo!')
