notas = (91, 29, 76, 8, 10, 58, 65, 13, 73, 23, 60, 54, 93, 60, 73, 52, 54, 75, 83, 68, 75, 28, 70, 45, 88, 51, 53)
soma = 0
for n in notas:
    soma += n / 10
    media = soma / len(notas)
print(f'A soma das {len(notas)} notas é {soma}')
print(f'A média das {len(notas)} notas é {media:.1f}')
print(f'A maior nota foi {max(notas) / 10}, na posição {notas.index(max(notas)) + 1}')
print(f'A menor nota foi {min(notas) / 10}, na posição {notas.index(min(notas)) + 1}')