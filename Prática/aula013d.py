# Exemplos funcionais:

# Loop com valor final definido pelo usuário.
n = int(input('Digite um número: '))
for c in range(0, n+1):
    print(c)
print('FIM')

# Loop com range definido pelo usuário.
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('FIM')

# Repetindo leitura 3 vezes.
for c in range(0, 3):
    n = int(input('Digite um valor: '))
print('FIM')

# Soma de 4 leituras.
s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print('O somatório de todos os valores são {}'.format(s))