preco = float(input('Qual é o preço do produto? R$'))
desconto5 = preco * 5 / 100
preco_com_desconto = preco - desconto5

print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar {:.2f}.'.format(
    preco, preco_com_desconto))
