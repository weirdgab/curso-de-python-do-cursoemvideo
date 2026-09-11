while True:
    n = int(input('Que ver a tabuada de qual valor? (Digite 0 para parar): '))
    if n <= 0:
        break
    print('-' * 30)
    for c in range(1, 11):
        print(f'{n} x {c} = {n * c}')
    print('-' * 30)
