numero = int(input('Digite um número para ver sua tabuada: '))
multiplicacao = 0

for c in range(1, 11):
    multiplicacao += 1
    resultado = numero * multiplicacao
    print('{} x {} = {}'.format(numero, multiplicacao, resultado))
