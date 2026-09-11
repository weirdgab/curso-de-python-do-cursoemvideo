import moeda_corrigido

p = float(input('Digite o preço: R$'))
print(
    f'A metade de {moeda_corrigido.moeda(p)} é {moeda_corrigido.metade(p, True)}')
print(
    f'O dobro de {moeda_corrigido.moeda(p)} é {moeda_corrigido.dobro(p, True)}')
print(
    f'Aumentando 10%, temos {moeda_corrigido.aumentar(p, 10, True)}')
print(f'Reduzindo 13%, temos {moeda_corrigido.diminuir(p, 13, True)}')
