import random

print('-=-' * 20, '\nVAMOS JOGAR PAR OU ÍMPAR')
print('-=-' * 20)

vitorias = 0
parada = 0

while parada == 0:
    nJogador = int(input('Digite um valor: '))
    nComputador = random.randint(1, 10)
    escolha = str(input('Par ou Ímpar? [P/I]')).strip().upper()
    while True:
        if escolha in 'PIÍ' or escolha == 'PAR' or escolha == 'IMPAR' or escolha == 'ÍMPAR':
            print(f'O computador escolheu {nComputador} e você {nJogador}')
            soma = nJogador + nComputador
            if escolha == 'P' or escolha == 'PAR':
                if soma % 2 == 0:
                    print(f'Você venceu! {soma} é PAR.')
                    vitorias += 1
                    break
                else:
                    print(f'GAME OVER...')
                    print(f'número de vitórias = {vitorias}')
                    parada = 1
                    break
            else:
                if escolha in 'IÍ' or escolha == 'IMPAR' or escolha == 'ÍMPAR':
                    if soma % 2 != 0:
                        print(f'Você venceu! {soma} é ÍMPAR.')
                        vitorias += 1
                        break
                    else:
                        print(f'GAME OVER...')
                        print(f'número de vitórias = {vitorias}')
                        parada = 1
                        break
        else:
            print('Valor digitado não reconhecido. Tente novamente')
