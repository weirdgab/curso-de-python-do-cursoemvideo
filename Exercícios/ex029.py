kmCorridos = int(input('Digite a velocidade média percorrida: '))
multa = (kmCorridos - 80) * 7

if kmCorridos > 80:
    print('Você ultrapassou o limite de velocidade! Sua multa é de {}R$.'.format(multa))
else:
    print('A velocidade média de {}Km/h está dentro dos limites.'.format(kmCorridos))