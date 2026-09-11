# Escopo de variáveis
def teste():
    x = 8
    print(f'Na função teste, n vale {n}.')  # Escopo global
    print(f'Na função teste, x vale {x}.')  # Escopo local


def teste2(b):
    global a  # global a diz para o python não criar uma cópia local, e sim usar "a" como global
    print(f'Variável "a" dentro vale {a}')
    a = 8
    b += 4
    c = 2
    print(f'Variável "a" dentro vale {a}')
    print(f'Variável "b" dentro vale {b}')
    print(f'Variável "c" dentro vale {c}')


# Programa principal
n = 2
print(f'No programa principal, n vale {n}.')
teste()
# "print(f'No programa principal, n vale {x}.')" gerará um erro de definição.
print('x não existe fora do escopo da função teste.')

a = 5
teste2(a)
print(f'Variável "a" fora vale {a}')
# "print(f'Variável "b" fora vale {b}')" gerará erro de definição.
# "print(f'Variável "c" fora vale {c}')" gerará erro de definição.
