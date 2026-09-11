import datetime

maiorIdade = 0
menorIdade = 0
ordem = 1

for c in range(1, 8):
    ano = int(input('Em que ano a {}º pessoa nasceu? '.format(ordem)))
    ordem += 1
    if datetime.date.today().year - ano >= 18:
        maiorIdade += 1
    else:
        menorIdade += 1
print('Nessa lista, {} pessoas são maiores de idades e {} são menores de idade.'.format(maiorIdade, menorIdade))
