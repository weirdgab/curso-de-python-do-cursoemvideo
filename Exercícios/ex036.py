print('-' * 20)
print('\033[34mCalculador de Empréstimo\033[m')
print('-' * 20)

casaValor = float(input('Qual o valor da casa? '))
salario = float(input('Qual o valor do seu salário? '))
prestacaoAno = float(input('Em quantos anos você deseja pagar? ')) * 12
prestacaoCalculo = casaValor / prestacaoAno
porcentagemLimite = (salario / 100) * 30

if prestacaoCalculo > porcentagemLimite:
    print(
        'Salário abaixo do permitido para esse número de parcelas. \nEmpréstimo \033[1;31mNEGADO\033[m')
else:
    print('Tudo certo por aqui. \nEmpréstimo \033[1;32mCONCLUÍDO\033[m')
