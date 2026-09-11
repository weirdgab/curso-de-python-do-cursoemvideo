from datetime import date
print('-' * 20)
print('\033[34mServiço Militar Obrigatório\033[m')
print('-' * 20)

anoNascimento = input('Qual sua data de nascimento? ')
verificacao = anoNascimento.isnumeric()
if verificacao:
    dataAtual = date.today().year
    anoNascimento = int(anoNascimento)
    idade = dataAtual - anoNascimento
    print('Idade atual: {} anos.'.format(idade))
    if idade == 18:
        print('Você está no período de alistamento militar, faça sua inscrição!')
    elif idade > 18:
        anosAcima = idade - 18
        print('Você deveria ter se alistado a {} ano(s). Caso não tenha ocorrido, regularize-se já!'.format(anosAcima))
    else:
        anosAbaixo = 18 - idade
        if anosAbaixo == 1:
            print('Falta {} ano para seu alistamento militar, tenha um bom dia!'.format(
                anosAbaixo))
        else:
            print('Faltam {} anos para seu alistamento militar, tenha um bom dia!'.format(
                anosAbaixo))
else:
    print(
        '\033[1;31mERRO\033[m, valor digitado não reconhecido. Por favor reiniciar o programa.')
