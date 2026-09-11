def leiaint(string):
    n = input(string)
    while n.isnumeric() == False:
        print('\033[31mERRO! Digite um número inteiro válido.\033[m')
        n = input(string)
    n = int(n)
    return n


# Programa Principal
n = leiaint('Digite um número: ')
print(f'O número digitado foi {n}.')
