print('=' * 20)
print('\033[1mLOJAS GUANABARA\033[m')

precoCompras = float(input('Preço das compras R$ '))

descontoDinheiroCheque = precoCompras / 100 * 10
descontoCartao = precoCompras / 100 * 5
jurosCartao = precoCompras / 100 * 20


print('\nSelecione a forma de pagamento: ')
print('[1] Dinheiro')
print('[2] Cheque')
print('[3] Cartão\n')

opcao = int(input('Opção desejada: '))

if opcao == 1 or opcao == 2:
    print('\nDesconto de 10% aplicado, valor total: {}\n'.format(
        precoCompras - descontoDinheiroCheque))
    print('Tenha um bom dia!')
elif opcao == 3:
    print('\nCrédito ou Débito?')
    print('[1] Crédito')
    print('[2] Débito\n')
    pagamento = int(input('Opção desejada:'))
    if pagamento == 1 or 2:
        parcelas = int(input('Digite o número de parcelas: '))
        if parcelas == 1:
            print('\nDesconto de 10% aplicado, valor total: {}').format(
                precoCompras - descontoDinheiroCheque)
            print('Tenha um bom dia!\n')
        elif parcelas == 2:
            print('Você pagará duas parcelas no valor de {}.'.format(precoCompras / parcelas))
            print('Tenha um bom dia!\n')
        elif parcelas >= 3:
            juros = precoCompras + jurosCartao
            valorParcelas = juros / parcelas
            print('\nJuros de 20% aplicado.')
            print('Você pagará {} parcelas no valor de {}.\nO valor total será: {}\n'.format(
                parcelas, valorParcelas, juros))
else:
    print('Opção desejada não reconhecida. Por favor reinicie o programa.\n')
