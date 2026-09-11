salario = float(input('Qual é o salário de um funcionário? R$'))
aumento5 = salario * 15 / 100
novo_salario = salario + aumento5

print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}.'.format(
    salario, novo_salario))
