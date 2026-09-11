def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:>.2f}'.replace('.', ',')


def aumentar(preco=0, taxa=0, conver=False):
    res = preco + (preco * taxa/100)
    if conver == True:
        return moeda(res)
    else:
        return res


def diminuir(preco=0, taxa=0, conver=False):
    res = preco - (preco * taxa/100)
    if conver == True:
        return moeda(res)
    else:
        return res


def dobro(preco=0, conver=True):
    res = preco * 2
    if conver == True:
        return moeda(res)
    else:
        return res


def metade(preco=0, conver=True):
    res = preco / 2
    if conver == True:
        return moeda(res)
    else:
        return res
