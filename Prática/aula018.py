# Criando matrizes (listas de listas)

# Imprimindo com cópias cria múltiplas listas internas com uma única variável.
teste = list()
teste.append('Gustavo')
teste.append(40)

galera = list()
galera.append(teste[:])

teste[0] = 'Maria'
teste[1] = 22

galera.append(teste[:])
print(galera)

# Imprimindo sem cópias cria uma única lista interna interligada.
teste = list()
teste.append('Gustavo')
teste.append(40)

galera = list()
galera.append(teste)

teste[0] = 'Maria'
teste[1] = 22

galera.append(teste)
print(galera)
