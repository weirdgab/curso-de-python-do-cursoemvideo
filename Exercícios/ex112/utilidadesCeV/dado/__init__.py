def leiaDinheiro():
    preco = input('Digite o preço: R$').strip()
    while preco.isnumeric == False:
        print('\033[0:31mERRO!\033[0:31m Valor informado inválido.')
        preco = input('Digite o preco: R$')
    return float(preco)
