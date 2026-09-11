dias_usados = float(input('Quantos dias foram usados? ')) * 60
km_rodados = float(input('Quantos KMs foram rodados? ')) * 0.15
preco = dias_usados + km_rodados

print('O valor do aluguel é R${:.2f}'.format(preco))
