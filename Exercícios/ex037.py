print('Escolha uma das opções abaixo para converter seu número.')
print('[1] - Para hexadecimal.\n[2] - Para Binário.\n[3] - Para octal.')
opcao = int(input('Digite sua opção escolhida: '))

if opcao == 1:
    numero = int(input('Digite um número inteiro a ser convertido: '))
    print('{} convertido para hexadecimal é igual a {}'.format(numero, hex(numero)))
elif opcao == 2:
    numero = int(input('Digite um número inteiro a ser convertido: '))
    print('{} convertido para binário é igual a {}'.format(numero, bin(numero)))
elif opcao == 3:
    numero = int(input('Digite um número inteiro a ser convertido: '))
    print('{} convertido para octal é igual a {}'.format(numero, oct(numero)))
else:
    print('Valor digitado não indentificado. Por favor reinicie o programa.')
