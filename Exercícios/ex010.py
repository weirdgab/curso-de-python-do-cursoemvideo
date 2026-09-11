saldo = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = 3.27
saldo_convertido = saldo / dolar

print('Com essa quantia você poderia comprar US${:.2f}.'.format(
    saldo_convertido))
