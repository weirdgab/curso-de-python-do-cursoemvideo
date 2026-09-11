numeros = []
numerosPares = []
numerosImpares = []
numeroNovo = -1
checagem = "teste"

while True:
    if checagem in "nNnaoNAOnãoNÃO":
        break
    numeroNovo = int(input(
        "Digite o número que deseja adicionar a lista: "))
    numeros.append(numeroNovo)
    checagem = str(input("Deseja continuar? [s/n]: "))
    if checagem in "sSsimSIM":
        pass
    elif checagem in "nNnaoNAOnãoNÃO":
        break
    else:
        while True:
            print("Opção escolhida não identificada, tente novamente.")
            checagem = str(input("Deseja continuar? [s/n]: "))
            if checagem in "sSsimSIM":
                break

numerosTeste = numeros[:]

for c in range(0, len(numeros)):
    if numerosTeste[-1] % 2 == 0:
        numerosPares.append(numerosTeste[-1])
        numerosTeste.pop()
    else:
        numerosImpares.append(numerosTeste[-1])
        numerosTeste.pop()

numerosPares.sort()
numerosImpares.sort()

print(f'A lista completa foi: {numeros}')
print(f'A lista somente com os números pares foi: {numerosPares}')
print(f'A lista somente com os números ímpares foi: {numerosImpares}')
