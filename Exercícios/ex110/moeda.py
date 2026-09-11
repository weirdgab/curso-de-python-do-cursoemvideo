def aumentar(preco=0, taxa=0):
    res = moeda(preco + (preco * taxa/100))
    return res


def diminuir(preco=0, taxa=0):
    res = moeda(preco - (preco * taxa/100))
    return res


def dobro(preco=0):
    res = moeda(preco * 2)
    return res


def metade(preco=0):
    res = moeda(preco / 2)
    return res


def moeda(preco=0, moeda='R$'):
    return f'{moeda:>5}{preco:.2f}'.replace('.', ',')


def resumo(preco=0, aum=0, red=0):
    print('-' * 30)
    print('     RESUMO DO VALOR')
    print('-' * 30)
    print(f'Preço analisado:   {moeda(preco)}')
    print(f'Dobro do preço:    {dobro(preco)}')
    print(f'Metade do preço:   {metade(preco)}')
    print(f'{aum}% de aumento:{'':<5}{aumentar(preco, aum)}')
    print(f'{dim}% de aumento:{'':<5}{diminuir(preco, dim)}')
    print('-' * 30)
