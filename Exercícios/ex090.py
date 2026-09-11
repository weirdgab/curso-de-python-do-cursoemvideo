situacao = dict()
situacao['Nome'] = str(input('Nome: '))
situacao['Média'] = float(input(f'Média de {situacao['Nome']}: '))

print('-=' * 30)

if situacao['Média'] >= 7:
    situacao['Situação'] = 'Aprovado'
elif situacao['Média'] < 5:
    situacao['Situação'] = 'Reprovado'
else:
    situacao['Situação'] = 'Recuperação'

for k, v in situacao.items():
    print(' ' * 5, f'- {k} é igual a {v}')
