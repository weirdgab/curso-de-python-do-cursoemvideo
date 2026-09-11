print('=' * 20, '\nSuper Progressão Aritmética:')
print('=' * 20)

primeiroTermo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
cont = 0
quantTermos = 1
totalTermos = 10

while quantTermos != 0:
    print(primeiroTermo, end=' ')
    primeiroTermo += razao
    cont += 1
    if cont == 10:
        print('PAUSA')
        while quantTermos != 0:
            quantTermos = int(input('Quantos termos você quer mostrar a mais? '))
            totalTermos += quantTermos
            for c in range(1, quantTermos + 1):
                print(primeiroTermo, end=' ')
                primeiroTermo += razao
            print('| Mais {} termos adicionados.'.format(quantTermos))
print('O total de termos adicionados foi {} termos.'.format(totalTermos))
print('Fim do programa')
