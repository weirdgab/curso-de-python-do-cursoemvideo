print('-' * 20)
print('\033[1mPrograma para Cálculo do \033[1;34mIMC\033[m\033[1m:\033[m')
print('-' * 20)

altura = float(input('Digite sua altura em centímetros: '))
peso = float(input('Digite seu peso: '))
imc = peso / ((altura / 100) ** 2)

if imc < 18.5:
    print('Seu IMC é: \033[34m{:.2f}\033[m.'.format(imc))
    print('Você está \033[31mABAIXO DO PESO\033[m!')
elif imc <= 25:
    print('Seu IMC é: \033[34m{:.2f}\033[m.'.format(imc))
    print('Você está no \033[32mPESO IDEAL\033[m!')
elif imc <= 30:
    print('Seu IMC é: \033[34m{:.2f}\033[m.'.format(imc))
    print('Você está com \033[33mSOBREPESO\033[m, cuidado!')
elif imc <= 40:
    print('Seu IMC é: \033[34m{:.2f}\033[m.'.format(imc))
    print('Você está com \033[31mOBESIDADE\033[m!')
else:
    print('Seu IMC é: \033[34m{:.2f}\033[m.'.format(imc))
    print('Você está com \033[7;30mOBESIDADE MÓRBIDA\033[m, procure um médico imediatamente!')
