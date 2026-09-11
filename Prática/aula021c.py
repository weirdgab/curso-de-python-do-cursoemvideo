# Parâmetros opcionais
# c é um parâmetro opcional, se não receber valor ele recebe zero.
def somar(a, b, c=0):
    s = a + b + c
    print(f'A soma vale {s}')
# TODOS PODEM SER PARÂMETROS OPCIONAIS!!!


somar(3, 2, 5)
somar(8, 4)
