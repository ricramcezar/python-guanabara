soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1 # contador soma 1
        soma += c # acumulador soma um valor
print(f'A soma de todos os {cont} valores solicitados é {soma}.')
