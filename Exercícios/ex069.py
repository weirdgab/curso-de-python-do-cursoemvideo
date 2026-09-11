pessoasMais18 = 0
totalHomens = 0
mulheresMenos20 = 0
contagem = 1

while True:
    print('=' * 22, '\nCADASTRO DA {}º PESSOA:'.format(contagem))
    print('=' * 22)
    genero = str(input('Gênero (NB para não binário): ')).lower().strip()
    if genero == 'masculino' or genero == 'm':
        totalHomens += 1
    idade = str(input('Idade: ')).strip()
    while idade.isdigit() == False or idade == '0':
        print(f'O valor {idade} não é uma idade válida.')
        print('Por favor, entre com uma idade válida.')
        idade = str(input('Idade: ')).strip()
    idade = int(idade)
    if idade > 18:
        pessoasMais18 += 1
    if genero == 'f' or genero == 'feminino':
        if idade < 20:
            mulheresMenos20 += 1
    print('Pessoa cadastrada com sucesso! ')
    contagem += 1
    resposta = str(input(
        'Deseja cadastrar outra pessoa? [N/S]: ')).strip().upper()
    if resposta == 'N' or resposta == 'NÃO':
        break


print('Total de pessoas com mais de 18 anos cadastradas: ', pessoasMais18)
print('Total de mulheres com menos de 20 anos cadastradas: ', mulheresMenos20)
print('Total de homens cadastrados: ', totalHomens)
