salario = float(input('Qual é o salário do funcionário: R$'))

if salario >= 1250:
    aumento = salario * 1.10 # ou aumento = salario + (salario * 15 / 100)
else:
    aumento = salario * 1.15 # ou aumento = salario + (salario * 10 / 100)

print(f'Quem ganhava R${salario:.2f} passa a ganhar R${aumento:.2f} agora.')