soma_idade = 0
media_idade = 0
maior_idade_homem = 0
nome_mais_velho = ''
total_mulher_20 = 0
for p in range(1, 5):
    print(f'----- {p}ª PESSOA -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    soma_idade += idade
    if p == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_mais_velho = nome
    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_mais_velho = nome
    if sexo in 'Ff' and idade < 20:
        total_mulher_20 += 1
media_idade = soma_idade / 4
print(f'A média de idade do grupo é de {media_idade} anos.')
print(f'O homem mais velho tem {maior_idade_homem} anos e se chama {nome_mais_velho}.')
if total_mulher_20 == 1:
    print(f'Ao todo há {total_mulher_20} mulher com menos de 20 anos.')
else:
    print(f'Ao todo há {total_mulher_20} mulheres com menos de 20 anos.')
