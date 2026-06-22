cidade = str(input('Em que cidade você nasceu? ').strip())
print(cidade[:5].upper() == 'SANTO')

# ALTERNATIVAMENTE:
# cidade = str(input('Em que cidade você nasceu? ').strip().upper())
# print('SANTO' in cidade)