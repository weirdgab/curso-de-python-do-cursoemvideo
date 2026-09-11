numero = int(input('Digite um número para calcular seu fatorial: '))
fatorial = 0
texto = ''
numeroTexto = 0

while numero != 1:
    if numeroTexto == 0:
        numeroTexto += numero
    if fatorial == 0:
        fatorial = numero * (numero - 1)
    else:
        fatorial = fatorial * (numero - 1)
    numero -= 1
    texto = texto + ' x {}'.format(numero)


print('O fatorial de {} é igual a {}{} = {}'.format(numeroTexto, numeroTexto, texto, fatorial))
