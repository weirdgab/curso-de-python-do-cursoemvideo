pessoas = list()
dados = list()
maisLeve = maisPesada = 0
maiorPeso = menorPeso = 0
totpessoas = 0

verificacao = 's'
while verificacao in 'sS':
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    totpessoas += 1
    verificacao = str(input('Deseja continuar? [s/n] '))

print(f'Ao todo você cadastrou {totpessoas} pessoas.')

for c, v in enumerate(pessoas):
    if c == 0:
        maisLeve = maisPesada = v[0]
        maiorPeso = menorPeso = v[1]
    else:
        if v[1] > maiorPeso:
            maisPesada = v[0]
            maiorPeso = v[1]
        elif v[1] == maiorPeso:
            maisPesada += ' ' + v[0]
            maiorPeso = v[1]

        if v[1] < menorPeso:
            maisLeve = v[0]
            menorPeso = v[1]
        elif v[1] == menorPeso:
            maisLeve += ' ' + v[0]
            menorPeso = v[1]

print(f'A pessoa mais pesada foi {maisPesada} pesando {maiorPeso} kilos')
print(f'A pessoa mais leve foi {maisLeve} pesando {menorPeso} kilos')
