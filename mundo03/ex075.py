valor = 0
cont = 1
valores = ()
for _ in range(4):
    valor = int(input(f'Digite o {cont}º valor: '))
    cont += 1
    valores += (valor,)
print(f'Você digitou os valores {valores}')
print(f'O valor 9 apareceu {valores.count(9)} vezes.')
if 3 in valores:
    print(f'O valor 3 apareceu na {valores.index(3) + 1}ª posição.')
else:
    print('O valor 3 não foi digitado em nenhuma posição.')
print('Os valores pares digitados foram ', end='')
for v in valores:
    if v % 2 == 0:
        print(v, end = ' ')
