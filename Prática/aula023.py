# Sintaxe básica para tratamento de erros
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except:
    print('Infelizmente tivemos um problema :(')
print(f'O resultado é {r:.1f}')
