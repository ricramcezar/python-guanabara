temp_list = []
main_list = []
maior = menor = 0
while True:
    temp_list.append(str(input('Nome: ')))
    temp_list.append(float(input('Peso: ')))
    if len(main_list) == 0:
        maior = menor = temp_list[1]
    else:
        if temp_list[1] > maior:
            maior = temp_list[1]
        if temp_list[1] < menor:
            menor = temp_list[1]
    main_list.append(temp_list[:])
    temp_list.clear()
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Ao todo foram cadastradas {len(main_list)} pessoas. ')
print(f'O maior peso foi de {maior} kg. Peso de ', end='')
for p in main_list:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {menor} kg. Peso de ', end='')
for p in main_list:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')
