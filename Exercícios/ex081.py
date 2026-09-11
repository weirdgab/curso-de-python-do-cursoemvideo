numeros = []
numeroNovo = -1
checagem = "teste"

while True:
    if checagem in "nNnaoNAOnãoNÃO":
        break
    if numeroNovo == -1:
        numeroNovo = int(input(
            "Digite o número que deseja adicionar a lista: "))
        numeros.append(numeroNovo)
    else:
        numeroNovo = int(input(
            "Digite o número que deseja adicionar a lista: "))
        while numeroNovo in numeros:
            print("Este número já foi adicionado, tente adicionar um número diferente!")
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

print(f'Foram digitados {len(numeros)} valores.')
numeros.sort(reverse=True)
print(f"Os números adicionados em ordem decrescente foram: {numeros}")
if 5 in numeros:
    print('O número 5 está na lista.')
else:
    print('O número 5 não está na lista.')
