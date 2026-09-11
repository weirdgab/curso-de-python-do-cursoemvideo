nome = str(input('Qual é seu nome completo? ')).strip()
nomeMinusculo = nome.lower()

print('Seu nome tem Silva?', nomeMinusculo.find('silva') > -1)
