print('=' * 20, 'Programa de Manipulação de Números', '=' * 20)
print('[1] Somar')
print('[2] Subtrair')
print('[3] Multiplicar')
print('[4] Dividir')
print('[5] Potenciar')
print('[6] Comparação')
print('[7] Sair do Programa')
print('=' * 76)

opcao = 0
while opcao != 7:
    opcao = input('\nDigite a opção desejada: ')
    if opcao.isnumeric() == True:
        if opcao == 1:
            numero1 = float(input('Digite o primeiro número da soma: '))
            numero2 = float(input('Digite o segundo número da soma: '))
            soma = numero1 + numero1
            print('O resultado da soma dos números digitados é: {}'.format(soma))
        elif opcao == 2:
            numero1 = float(input('Digite o primeiro número da subtração: '))
            numero2 = float(input('Digite a quantia a ser subtraída: '))
            subtracao = numero1 - numero2
            print('O resultado da subtração dos números digitados dará: {}'.format(subtracao))
        elif opcao == 3:
            numero1 = float(input('Digite o primeiro número da multiplicação: '))
            numero2 = float(input('Digite o segundo número da multiplicação: '))
            multiplicacao = numero1 * numero2
            print('O resultado da multiplicação entre os números digitados é: {}'.format(multiplicacao))
        elif opcao == 4:
            numero1 = float(input('Digite o dividendo da divisão: '))
            if numero1 == 0:
                print('Você não pode dividir por zero!')
            else:
                numero2 = float(input('Digite o divisor da divisão: '))
                if numero2 == 0:
                    print('Você não pode dividir por zero!')
                else:
                    divisao = numero1 / numero2
                    print('A divisão entre os dois números digitados equivale a: {}'.format(divisao))
        elif opcao == 5:
            numero1 = float(input('Digite o número base: '))
            numero2 = float(input('Digite o valor para elevação do número base: '))
            potenciacao = numero1 ** numero2
            print('{} elevado a {} resultará em: {}'.format(numero1, numero2, potenciacao))
        elif opcao == 6:
            numero1 = float(input('Digite o primeiro número da comparação: '))
            numero2 = float(input('Digite o segundo número da comparação: '))
            if numero1 > numero2:
                print('O número {} é maior que {}'.format(numero1, numero2))
            elif numero1 < numero2:
                print('O número {} é menor que {}'.format(numero1, numero2))
            else:
                print('Os valores são iguais!')
        else:
            print('Opção inserida inválida. Tente novamente.')
    else:
        print('Opção digitada inválida. Tente novamente.')
print('Programa finalizado.')
