print('=' * 20)
print('10 Termos de uma PA')
print('=' * 20)

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

décimo = primeiro + (10 - 1) * razao

for c in range(primeiro, décimo + razao, razao):
    print('{} '.format(c), end='-> ')
print('ACABOU')
