import moeda

n = float(input('Digite um preço: R$'))
print(f'A metade de R${n} é {moeda.metade(n)}')
print(f'O dobro de R${n} é {moeda.dobro(n)}')
print(f'Aumentando 10%, temos R${moeda.aumentar(n)}')
print(f'Diminuindo 10%, temos R${moeda.diminuir(n)}')
