ordemPessoas = 1
nomeMaisVelho = ''
idadeMaisVelho = 0
mulheresSub20 = 0
mediaIdades = 0
contMulheres = 0
contHomens = 0


for c in range(1, 5):
    nome = str(input('Qual o nome da {}º pessoa? '.format(ordemPessoas)))
    idade = int(input('Qual a idade da {}º pessoa? '.format(ordemPessoas)))
    genero = str(
        input('Qual o gênero da {}º pessoa? (F para feminino e M para masculino) '.format(ordemPessoas))).upper()
    if genero == 'M':
        if c == 1:
            nomeMaisVelho = nome
            idadeMaisVelho = idade
        elif idadeMaisVelho < idade:
            idadeMaisVelho = idade
            nomeMaisVelho = nome
        contHomens += 1
    elif genero == 'F':
        if idade < 20:
            mulheresSub20 += 1
        contMulheres += 1
    ordemPessoas += 1
    mediaIdades += idade

print('A média das idades dos indivíduos é {:.2f}.'.format(mediaIdades / 4))
if contHomens > 0:
    print('O nome do homem mais velho é {} com o mesmo possuindo {} anos'.format(
        nomeMaisVelho, idadeMaisVelho))
if contMulheres > 0:
    print('Foi identificado {} mulher(es) com menos de 20 anos nos valores inseridos.'.format(mulheresSub20))
