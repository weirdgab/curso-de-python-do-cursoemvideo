# Iterando sobre a matriz
galera = list()
dado = list()
totmai = totmen = 0

# Estrutura de repetição para adição de valores a galera de forma sequencial e organizada
for c in range(0, 3):  # Processo é repetido por 3 vezes
    dado.append(str(input('Nome: ')))  # Adicionando valor "Nome" a lista dado
    dado.append(int(input('Idade: ')))  # Adicionando valor "Idade" a lista dado
    galera.append(dado[:])  # Salvando cópia de lista dado na matriz galera
    dado.clear()  # Apagando lista dado original

print(galera)

# Estrutura para verificar somente maiores de idade
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1

print(f'Temos {totmai} maiores e {totmen} menores de idade.')
