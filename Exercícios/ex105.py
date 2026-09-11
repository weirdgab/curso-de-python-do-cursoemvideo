def notas(* n, sit=False):
    """
        => Função para analisar notas e situações de vários alunos.
        :param n: uma ou mais notas dos alunos (aceita várias)
        :param sit: valor opcional, indicando se deve ou não adicionar a situação
        :return: dicionário com várias informações sobre a situação da turma.
    """
    ficha = dict()
    cont = maior = menor = soma = 0
    for valor in n:
        if cont == 0:
            maior = menor = valor
        else:
            if valor > maior:
                maior = valor
            if valor < menor:
                menor = valor
        soma += valor
        cont += 1
    ficha['total'] = cont
    ficha['maior'] = maior
    ficha['menor'] = menor
    ficha['média'] = soma / len(n)
    if sit == True:
        if ficha['média'] < 6:
            ficha['situação'] = 'RUIM'
        elif ficha['média'] > 7:
            ficha['situação'] = 'BOA'
        else:
            ficha['situação'] = 'RAZOÁVEL'
    return ficha


resp = notas(9, 8, 7, 9, sit=True)
print(resp)
help(notas)
