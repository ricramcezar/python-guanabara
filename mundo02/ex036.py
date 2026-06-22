valor = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestacao = valor / (anos * 12)

print(f'Para pagar uma casa de R${valor:.2f} em {anos} anos,\n'
      f'a prestação será de R${prestacao:.2f}')

if prestacao > (salario - (salario * 0.3)):
    print('Empréstimo NEGADO!')
else:
    print('Empréstimo pode ser CONCEDIDO!')