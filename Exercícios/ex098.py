def contagem(inicio, fim, passo):
    if passo == 0:
        passo = 1
    if inicio <= fim:
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
        for c in range(inicio, fim + 1, passo):
            print(f'{c} ', end='')
    elif inicio > fim and passo < 0:
        passo2 = passo * -1
        print(f'Contagem de {inicio} até {fim} de {passo2} em {passo2}')
        for c in range(inicio, fim - 1, passo):
            print(f'{c} ', end='')
    elif inicio > fim:
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
        for c in range(inicio, fim - 1, - passo):
            print(f'{c} ', end='')
    print('FIM!')
    print('-=' * 30)


print('-=' * 30)
contagem(1, 10, 1)
contagem(10, 0, -2)

print('Agora é sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

contagem(i, f, p)
