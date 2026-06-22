from datetime import date
ano_atual = date.today().year
total_maior = 0
total_menor = 0
for pessoa in range(1, 8):
    ano_nascimento = int(input(f'Em que ano a {pessoa}ª pessoa nasceu? '))
    idade = ano_atual - ano_nascimento
    if idade >= 21:
        total_maior += 1
    else:
        total_menor += 1
print(f'Ao todo tivemos {total_maior} pessoas maiores de idade.')
print(f'E também tivemos {total_menor} pessoas menores de idade.')