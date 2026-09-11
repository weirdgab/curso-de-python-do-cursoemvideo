ano = int(
    input('Que ano quer analisar? Coloque o 0 para analisar o ano atual: '))

if ano == 0:
    print('O ano de {} é não é bissexto.'.format(2025))
else:
    anoDezena = ano // 10 % 10
    if anoDezena == 00:
        if ano % 400 == 0:
            print('O ano de {} é bissexto.'.format(ano))
    else:
        divisao = anoDezena % 4
        if divisao == 0:
            print('O ano de {} é bissexto.'.format(ano))
        else:
            print('O ano de {} não é bissexto.'.format(ano))
