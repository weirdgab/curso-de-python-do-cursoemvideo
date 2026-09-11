print('-' * 20)
print('\033[1mPrograma de Formação de \033[32mTriângulos\033[m\033[1m:\033[m')
print('-' * 20)

a = float(input('Digite o primeiro segmento: '))
b = float(input('Digite o segundo segmento: '))
c = float(input('Digite o segundo segmento: '))

if a + b > c and a + c > b and b + c > a:
    if a == b and b == c:
        print('Os segmentos \033[32mPODEM\033[m formar um triângulo \033[33mEQUILÁTERO\033[m.')
    elif a == b or a == c or b == c:
        print('Os segmentos \033[32mPODEM\033[m formar um triângulo \033[33mISÓSCELES\033[m.')
    else:
        print('Os segmentos \033[32mPODEM\033[m formar um triângulo \033[33mESCALENO\033[m.')
else:
    print('Os segmentos \033[31mNÃO PODEM\033[m formar um triângulo\033[m.')