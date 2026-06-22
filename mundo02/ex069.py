tot18 = tot_homens = tot_mulher_20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        tot_homens += 1
    if sexo == 'F' and idade < 20:
        tot_mulher_20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}.')
print(f'Ao todo temos {tot_homens} homens cadastrados.')
if tot_mulher_20 == 1:
    print(f'E temos {tot_mulher_20} mulher com menos de 20 anos.')
else:
    print(f'E temos {tot_mulher_20} mulheres com menos de 20 anos.')