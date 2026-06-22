valor = 0
while True:
    print('-' * 30)
    valor = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 30)
    if valor < 0:
        break
    for n in range(1, 11):
        print(f'{valor} x {n} = {valor * n}')
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')