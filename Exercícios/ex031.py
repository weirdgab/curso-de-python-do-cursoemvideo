from time import sleep
distancia = float(input('Digite a distância da viagem em Kms: '))
print('Você está prestes a começar uma viagem de {}Km.'.format(distancia))

sleep(2)
if distancia <= 200:
    print('E o preço da viagem será de R${:.2f}'.format(distancia * 0.50))
else:
    print('E o preço da viagem será de R${:.2f}'.format(distancia * 0.45))
