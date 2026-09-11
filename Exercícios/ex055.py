ordem = 1
maiorPeso = 0
menorPeso = 0
pessoaMaisPesada = 0
pessoaMaisLeve = 0
pesosIguais = 0


for c in range(1, 6):
    pesoAtual = float(input('Qual o peso da {}º pessoa? '.format(ordem)))
    if menorPeso == 0:
        menorPeso += pesoAtual
        pessoaMaisLeve = ordem
    else:
        if pesoAtual < menorPeso:
            menorPeso = pesoAtual
            pessoaMaisLeve = ordem
    if pesoAtual > maiorPeso:
        maiorPeso = pesoAtual
        pessoaMaisPesada = ordem
    if pesoAtual == maiorPeso and pesoAtual == menorPeso:
        pesosIguais += 1
    ordem += 1

if pesosIguais == 5:
    print('Todos os pesos são iguais!')
else:
    print('O maior peso foi o da {}º pessoa, pesando {} kilos!'.format(pessoaMaisPesada, maiorPeso))
    print('E o menor peso foi o da {}º pessoa, pesando {} kilos!'.format(pessoaMaisLeve, menorPeso))
