preco = float(input('Qual é o preço do produto? R$'))
preco_desconto = preco - (preco * 5 / 100) 

print(f'O produto que custava R${preco:.2f}, na promoção com desconto de 5% vai custar R${preco_desconto:.2f}')