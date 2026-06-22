lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    resposta = str(input('Quer continuar? [S/N] '))
    if resposta in 'Nn':
        break
print('-=' * 30)
print(f'A lista completa é {lista}')
lista_pares = []
lista_impares = []
for n in lista:
    if n % 2 == 0:
        lista_pares.append(n)
    else:
        lista_impares.append(n)
lista_pares.sort()
lista_impares.sort()
print(f'A lista de pares é {lista_pares}')
print(f'A lista de ímpares é {lista_impares}')