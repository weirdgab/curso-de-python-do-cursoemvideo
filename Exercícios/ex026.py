nome = str(input('Digite seu nome: ')).strip()
nomeMinusculo = nome.lower()
print('Seu nome tem {} letras "A"'.format(nomeMinusculo.count('a')))
print('A primeira letra "A" aparece na posição {}.'.format(nomeMinusculo.find('a')))
