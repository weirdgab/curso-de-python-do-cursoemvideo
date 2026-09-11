print('=' * 20, '\nSequência de Fibonacci:')
print('=' * 20)

termos = 0
fibonacci = 0
fibonacci2 = 1

while termos == 0:
    termos = int(input('Quantos termos da sequência você quer mostrar? '))
    for c in range(1, termos + 1):
        print(fibonacci, end=' ')
        fibonacci, fibonacci2 = fibonacci2, fibonacci + fibonacci2
