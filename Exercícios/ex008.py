metros = float(input('Digite um valor em metros: '))
quilometro = metros / 1000
hectometro = metros / 100
decametro = metros / 10
decimetro = metros / 0.1
centimetro = metros / 0.01
milimetro = metros / 0.001
micrometo = metros / 0.000001
nanometro = metros / 0.000000001

print('{} metros equivale a:'.format(metros))

print('{} quilômetros. \n{} hectômetros. \n{} decâmetros \n{} centímetros. \n{} milímetros. \n{} micrômetros. \nE {} nanômetros.'.format(
    quilometro, hectometro, decametro, decimetro, centimetro, milimetro, micrometo, nanometro))
