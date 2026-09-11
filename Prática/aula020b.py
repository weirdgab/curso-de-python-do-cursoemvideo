# EMPACOTAMENTO DE PARÂMETROS
# "*" significa "desempacotar", função transformará valores em uma tupla.
def contador(* núm):
    for valor in núm:
        print(f'{valor} ', end='')
    print('FIM!')  # Exibirá valores sem parênteses seguidos de "FIM!".

    tam = len(núm)
    # Mostra tamanho de núm
    print(f'Recebi os valores {núm} e são ao todo {tam} números.')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)


def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}.')


soma(5, 2)
soma(2, 9, 4)
