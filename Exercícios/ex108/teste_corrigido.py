import moeda_corrigido

p = float(input('Digite o preço: R$'))
print(
    f'A metade de {moeda_corrigido.moeda(p)} é {moeda_corrigido.moeda(moeda_corrigido.metade(p))}')
print(
    f'O dobro de {moeda_corrigido.moeda(p)} é {moeda_corrigido.moeda(moeda_corrigido.dobro(p))}')
print(
    f'Aumentando 10%, temos {moeda_corrigido.moeda(moeda_corrigido.aumentar(p, 10))}')
