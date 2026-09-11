from random import randint
from time import sleep

print('-=--' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=--' * 20)

numero = int(input('Em que número eu pensei? '))
numeroAleatorio = randint(0, 5)
print('Processando...')
sleep(2)

if numero == numeroAleatorio:
    print('Resposta correta! Você acertou!')
else:
    print('Resposta errada eu pensei no número {}'.format(numeroAleatorio))
