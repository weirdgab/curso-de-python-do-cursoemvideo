salario = float(input('Qual é o salário do funcionário? R$'))
aumentoMin = (salario / 100) * 15
aumentoMax = (salario / 100) * 10

if salario <= 1250:
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(
        salario, salario + aumentoMin))
else:
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(
        salario, salario + aumentoMax))
