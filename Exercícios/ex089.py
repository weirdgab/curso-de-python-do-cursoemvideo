notas = []
boletim = []
aluno = []

verificacao = 's'

while verificacao not in 'nN':
    aluno.append(str(input('Nome do aluno: ')))
    notas.append(float(input('Primeira nota do aluno: ')))
    notas.append(float(input('Segunda nota do aluno: ')))

    aluno.append(notas[:])
    boletim.append(aluno[:])
    aluno.clear()
    notas.clear()

    verificacao = str(input('Deseja cadastrar mais um aluno? [S/n]: '))

verificacao2 = 's'
posicao = 0

while verificacao2 not in 'nN':
    print('-=' * 30)
    for c in range(0, len(boletim)):
        print(
            f'{c + 1} - {boletim[c][0]}, Média: {(boletim[c][1][0] + boletim[c][1][1]) / 2:.1f}')
    print('-=' * 30)

    verificacao2 = str(input('Deseja ver as notas individualmente? [S/n]: '))

    if verificacao2 not in 'nN':
        posicao = int(
            input('Digite o número do aluno que deseja consultar as notas: '))
        print(boletim[posicao - 1])
        verificacao2 = str(input('Deseja continuar? [S/n]: '))

print('Programa encerrado...')
