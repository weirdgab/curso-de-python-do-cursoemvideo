# ACESSANDO DICIONÁRIOS
pessoas = {'Nome': 'Gustavo', 'Sexo': 'M', 'Idade': '22'}

# IMPORTANTE: usar aspas duplas dentro de strings de aspas simples para acessar chaves de dicionários.

# Acessando chaves.
print(pessoas.keys())

# Acessando valores.
print(pessoas.values())

# Acessando items.
print(pessoas.items())

# Acessando de forma formatada.
print(f'O {pessoas["Nome"]} tem {pessoas["Idade"]} anos de idade e é do {pessoas["Sexo"]} de valor {pessoas["M"]}.')

# Acessando chaves por laços:
for k in pessoas.keys():
    print(k)

# Acessando valores por laços:
for v in pessoas.values():
    print(v)

# Acessando items por laços: (não possui mais o método enumerate)
for k, v in pessoas.items():
    print(f'{k} = {v}')
