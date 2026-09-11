while True:
    print('=' * 20)
    print('SIMULADOR DE CAIXA ELETRÔNICO')
    print('=' * 20)
    print('Cédulas disponíveis: R$50, R$20, R$10, R$1.')
    saque = int(input('Quanto você quer sacar? '))
    cedulas50 = saque // 50
    saque -= cedulas50 * 50
    cedulas20 = saque // 20
    saque -= cedulas20 * 20
    cedulas10 = saque // 10
    saque -= cedulas10 * 10
    print(
        f'Você receberá {cedulas50} cédulas de R$50,',
        f'{cedulas20} cédulas de R$20,',
        f'{cedulas10} cédulas de R$10 e {saque} cédulas de 1R$.')
    resposta = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if resposta == 'N':
        break
