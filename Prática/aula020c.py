# FUNÇÕES COM VALORES COMPOSTOS:
def dobra(lst):  # Valores compostos não precisam de desempacotamento.
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [7, 2, 5, 0, 4]
print(valores)  # Valores antes da chamada da função dobra.
dobra(valores)
print(valores)  # Valores após a chamada da função dobra.
