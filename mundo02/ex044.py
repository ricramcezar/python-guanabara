print(f'{' LOJAS GUANABARA ':=^40}')
preco = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual a opção? '))

if opcao == 1:
    novo_preco = preco - (preco * 0.10)
elif opcao == 2:
    novo_preco = preco - (preco * 0.05)
elif opcao == 3:
    novo_preco = preco
    parcela = novo_preco / 2
    print(f'Sua compra será parcelada em 2x de R${parcela:.2f} SEM JUROS')
elif opcao == 4:
    novo_preco = preco + (preco * 0.20)
    qtde_parcelas = int(input('Quantas parcelas? '))
    parcela = novo_preco / qtde_parcelas
    print(f'Sua compra será parcelada em {qtde_parcelas}x de {parcela:.2f} COM JUROS')
else:
    novo_preco = preco
    print('\n\033[30;41mOPÇÃO INVÁLIDA de pagamento. Tente novamente!\033[m')
print(f'Sua compra de R${preco:.2f} vai custar R${novo_preco:.2f} no final.')