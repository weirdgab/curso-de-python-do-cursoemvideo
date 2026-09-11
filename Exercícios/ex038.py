print('-' * 20)
print('\033[1;34mComparador de Números\033[m')
print('-' * 20)

n1 = input('Digite um número: ')
verificacao1 = n1.isnumeric()


if verificacao1:
    n2 = input('Digite outro número: ')
    verificacao2 = n2.isnumeric()
    if verificacao2:
        if n1 > n2:
            print('{} é \033[1;31mMAIOR\033[m que {}.'.format(
                float(n1), float(n2)))
        elif n2 > n1:
            print('{} é \033[1;32mMENOR\033[m que {}'.format(
                float(n1), float(n2)))
        elif n1 == n2:
            print('Os números {} e {} são \033[1;33mIGUAIS\033[m')
    else:
        print('Valor digitado não reconhecido. Por favor reinicie o programa.')
else:
    print('Valor digitado não reconhecido. Por favor reinicie o programa.')
