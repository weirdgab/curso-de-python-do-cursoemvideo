# DEFINIÇÃO E CHAMADA DE FUNÇÕES
def soma(a, b):  # O que há nos parênteses são parâmetros
    s = a + b
    print(s)


# Programa principal
soma(4, 5)
soma(8, 9)
soma(2, 1)
soma(a=3, b=7)  # Comando válido
soma(b=5, a=3)  # Comando válido, a ordem foi mudada

# soma(b=4, 5) não funcionaria pois se um parâmetro for explicitado todos também devem ser
# soma(4) ou soma(4, 5, 9) não funcionariam pois a função exige dois parâmetros, nem mais nem menos.
