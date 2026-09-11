totalGasto = 0
custamMaisDe1000 = 0
produtoMaisBarato = ''
menorPreco = 0
cont = 0


while True:
    print('=' * 20)
    print('MERCADINHO FULANO DE TAL')
    print('=' * 20)
    cont += 1
    nome = str(input('Qual é o nome do produto? ')).strip()
    preco = float(input('Qual é o preço dele? R$'))
    totalGasto += preco
    if preco > 1000:
        custamMaisDe1000 += 1
    if cont == 1:
        menorPreco = preco
    else:
        if preco < menorPreco:
            menorPreco = preco
            produtoMaisBarato = nome
    resposta = str(input('Deseja continuar? [S/N] ')).upper().strip()
    if resposta == 'N':
        break

print(f'O produto mais barato foi {produtoMaisBarato} custando {menorPreco}.')
print(f'O gasto total foi {totalGasto}')
print(f'{custamMaisDe1000} produtos custaram mais de R$1000')
