from datetime import date

cadastro = {'nome': str(input('Nome: ')), 'idade': int(input(
    'Ano de Nascimento: ')), 'ctps': int(input('Carteira de Trabalho (0 não tem): '))}

nascimento = cadastro['idade']
idade = date.today().year - cadastro['idade']
cadastro['idade'] = idade

if cadastro['ctps'] != 0:
    cadastro['contratacao'] = int(input('Ano de Contratação: '))
    cadastro['salario'] = float(input('Salário: R$'))
    cadastro['aposentadoria'] = (cadastro['contratacao'] - nascimento) + 35

print('-=' * 30)
for k, v in cadastro.items():
    print(f'   - {k} tem o valor {v}')
