# Condição aninhada sem else
nome = str(input('Qual é seu nome? '))
if nome == 'Gabriel':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Claúdia Jéssica Juliana':
    print('Belo nome feminino!')
print('Tenha um bom dia!')
