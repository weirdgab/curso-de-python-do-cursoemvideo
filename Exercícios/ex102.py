def fatorial(n=1, show=False):
    """
        -> Calcula o Fatorial de um número.
        :param n: O número a ser calculado.
        :param show: (opcional) Mostrar ou não a conta.
        :return: O valor do Fatorial de um número n.
    """
    if show == True:
        print(n, end=' ')
        for c in range(n - 1, 0, -1):
            print(f'x {c} ', end='')
    f = 1
    for c in range(n, 0, -1):
        f *= c
    if show == True:
        print(f'= ', end='')
    return f


print(fatorial(5, show=True))
help(fatorial)
