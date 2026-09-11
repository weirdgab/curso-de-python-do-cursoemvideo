dados = dict()
pessoas = list()
resp = 's'
totidade = 0
mulheres = list()
idademaiormedia = list()

while resp not in 'nN':
    dados['nome'] = str(input('Nome: '))
    dados['sexo'] = str(input('Sexo: [M/F] '))
    while dados['sexo'] not in 'mMfF':
        print('ERRO! Por favor, digite apenas M ou F.')
        dados['sexo'] = str(input('Sexo: [M/F] '))
    dados['idade'] = int(input('Idade: '))
    pessoas.append(dados.copy())
    print(pessoas)
    resp = str(input('Quer continuar? [S/n] '))
    while resp not in 'sSNn':
        print('ERRO! Responda apenas S ou N.')
        resp = str(input('Quer continuar? [S/n] '))

print('-=' * 30)
print(f'A) Ao todo temos {len(pessoas)} pessoa(s) cadastrada(s).')

for c in range(0, len(pessoas)):
    totidade += pessoas[c]['idade']

media = totidade / len(pessoas)
print(f'B) A média de idades é de {media:.2f} anos.')

for i, v in enumerate(pessoas):
    if pessoas[i]['sexo'] in 'fF':
        mulheres.append(pessoas[i]['nome'])

print(f'C) A mulheres cadastradas foram ', end='')
for c in range(0, len(mulheres)):
    print(mulheres[c], end=', ')
print()

for i, v in enumerate(pessoas):
    if pessoas[i]['idade'] > media:
        idademaiormedia.append(pessoas[i])
print(f'D) A lista de pessoas que estão acima da média: ')
for c in range(0, len(idademaiormedia)):
    print('    ', end='')
    for k, v in idademaiormedia[c].items():
        print(f'{k} = {v};', end=' ')
    print()

print('<< ENCERRADO >>')
