nome = input('Digite seu nome completo: ')

print('Analisando seu nome...')
print('Seu nome em maiúsculas é: ', nome.upper())
print('Seu nome em minúsculas é: ', nome.lower())
print('Seu nome tem ao todo {} letras.'.format(len(nome)))

primeiroNome = nome.split()

print('Seu primeiro nome é {} e ele tem {} letras.'.format(
    primeiroNome[0], len(primeiroNome[0])))
