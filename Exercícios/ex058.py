import random

numeroPC = random.randint(1, 10)
numeroUsuario = 0
palpites = 0

print('Acabei de pensar em um número, tente adivinhar...')

while numeroUsuario != numeroPC:
    numeroUsuario = int(input('Qual é seu palpite? '))
    if numeroUsuario > numeroPC:
        print('Menos... Tente novamente.')
    elif numeroUsuario < numeroPC:
        print('Mais... Tente novamente.')
    palpites += 1

print('Você acertou! O número que eu pensei era {}.'.format(numeroPC))
if palpites > 1:
    print('Foram necessários {} palpites!'.format(palpites))
elif palpites == 1:
    print('Você acertou de primeira!')
