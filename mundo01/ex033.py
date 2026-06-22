a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

valores = [a, b, c]

# ALTERNATIVAMENTE
# menor = a
# if b < a and b < c:
#     menor = b
# if c < a and c < b:
#     menor = c

# maior = a
# if b > a and b > c:
#     maior = b
# if c > a and c > b:
#     maior = c

print(f'O menor valor digitado foi {min(valores)}')
print(f'O maior valor digitado foi {max(valores)}')


