def leiaInt(msg):
    while True:
        try:
            numero = int(input(msg))
            return numero
        except KeyboardInterrupt:
            print(
                '\n\033[0;31mERRO! O usuário preferiu encerrar o programa.\033[m')
            return 0
            break
        except:
            print(
                '\033[0;31mERRO! O valor digitado não é um número inteiro válido\033[m')


def leiaFloat(msg):
    while True:
        try:
            numero = float(input(msg))
            return numero
        except KeyboardInterrupt:
            print(
                '\n\033[0;31mERRO! O usuário preferiu encerrar o programa.\033[m')
            return 0
            break
        except:
            print(
                '\033[0;31mERRO! O valor digitado não é um número real válido\033[m')


inteiro = leiaInt('Digite um número inteiro: ')
real = leiaFloat('Digite um número real: ')

print(f'O valor inteiro digitado foi {inteiro} e o valor real foi {real}')
