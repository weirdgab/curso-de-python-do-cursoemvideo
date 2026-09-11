numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
           'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    numeroUsuario = int(input('Digite um número entre zero e vinte: '))
    while numeroUsuario > 20 or numeroUsuario < 0:
        numeroUsuario = int(input(
            'Número digitado não reconhecido, tente novamente. Digite um número entre zero e vinte: '))
    print(f'O número digitado foi {numeros[numeroUsuario]}.')
    resposta = str(input('Quer continuar? '))
    if resposta in 'Nn':
        break
