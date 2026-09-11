from time import sleep
import random

print('=' * 20)
print(' ' * 5, '\033[35mJOKENPÔ\033[m')
print('=' * 20, '\n')

print('[1] = Pedra')
print('[2] = Papel')
print('[3] = Tesoura\n')

opcao = int(input('Escolha a opção desejada: '))

if opcao > 0 and opcao < 4:
    if opcao == 1:
        print('Você escolheu \033[30mPEDRA\033[m.')
    elif opcao == 2:
        print('Você escolheu \033[30mPAPEL\033[m.')
    elif opcao == 3:
        print('Você escolheu \033[30mTESOURA\033[m.')

    print('\nIniciando partida...')
    sleep(1)
    print('\033[34mJO\033[m')
    sleep(1)
    print('\033[34mKEN\033[m')
    sleep(1)
    print('\033[34mPÔ!\033[m\n')

    # Parte lógica:

    numeroAleatorio = random.randint(1, 3)

    if opcao == 1 and numeroAleatorio == 2:
        print('Você \033[31mPERDEU!\033[m, o computador escolheu \033[33mPAPEL\033[m.')
    elif opcao == 1 and numeroAleatorio == 3:
        print('Você \033[32mGANHOU!\033[m, o computador escolheu \033[33mTESOURA\033[m.')
    elif opcao == 2 and numeroAleatorio == 1:
        print('Você \033[31mGANHOU!\033[m, o computador escolheu \033[33mPEDRA\033[m.')
    elif opcao == 2 and numeroAleatorio == 3:
        print('Você \033[31mPERDEU!\033[m, o computador escolheu \033[33mTESOURA\033[m.')
    elif opcao == 3 and numeroAleatorio == 1:
        print('Você \033[31mPERDEU!\033[m, o computador escolheu \033[33mPEDRA\033[m.')
    elif opcao == 3 and numeroAleatorio == 2:
        print('Você \033[31mGANHOU!\033[m, o computador escolheu \033[33mPAPEL\033[m.')
    elif opcao == numeroAleatorio:
        print('Parece que deu um \033[37mEMPATE!\033[m')
    print('=' * 20)

else:
    print('Opção selecionada não reconhecida.\nPor favor reinicie o programa.')
