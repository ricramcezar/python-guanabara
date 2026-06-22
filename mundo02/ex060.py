# from math import factorial

# num = int(input('Digite um número para\n'
#                 'calcular seu Fatorial: '))
# fatorial = factorial(num)


num = int(input('Digite um número para calcular seu Fatorial: '))
cont = num
fatorial = 1 # usado para multiplicações
print(f'Calculando {num}! = ', end = '')
while cont > 0:
    print(f'{cont}', end = '')
    print(' x ' if cont > 1 else ' = ', end = '')
    fatorial *= cont
    cont -= 1
print(f'{fatorial}.')