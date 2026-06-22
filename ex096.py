def area(largura, comprimento):
    total_area = largura * comprimento
    print(f'A área de um terreno {largura}x{comprimento} é de {total_area}m².')


print('Controle de Terrenos')
print('-' * 20)
larg = float(input('LARGURA (m): '))
comp = float(input('COMPRIMENTO(m): '))
area(larg, comp)
