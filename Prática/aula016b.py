lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(lanche)

# Loops com tuplas
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')

# Comprimento da tupla
print(len(lanche))

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
