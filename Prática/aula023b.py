# No código anterior recebíamos um erro no bloco fora do tratamento
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except:
    print('Infelizmente tivemos um problema :(')
else:  # Paramos resolver usamos uma estrutura condicional caso a primeira verificação não seja concluída sem falhas
    print(f'O resultado é {r:.1f}')
