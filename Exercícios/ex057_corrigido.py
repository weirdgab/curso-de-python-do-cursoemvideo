sexo = str(input('Informe seu sexo: [M/F/N] ')).strip().upper()[0]
while sexo not in 'MmFfNn':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso.'.format(sexo))
