# LISTAS E DICIONÁRIOS

# Lista de dicionários.
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)

# Acessando "Rio de Janeiro".
print(brasil[0]['uf'])

# Acessando "SP".
print(brasil[1]['sigla'])

estado = dict()
estados_unidos = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    # Dicionários usam o método copy, não fazem fatiamento.
    estados_unidos.append(estado.copy())
    estado.clear()

for e in estados_unidos:
    for c in e.items():
        print(f'O estado {e['uf']} tem a sigla {e['sigla']}.')
