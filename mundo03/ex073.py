times = ('Flamengo', 'Palmeiras', 'Cruzeiro', 'Mirassol', 'Fluminense', 'Botafogo', 
         'Bahia', 'São Paulo', 'Grêmio', 'Bragantino', 'Atlético-MG', 'Santos', 
         'Corinthians', 'Vasco da Gama', 'EC Vitória', 'Internacional', 'Ceará SC', 
         'Fortaleza', 'Juventude', 'Sport Recife')

print('-=' * 30)
print(f'Lista de times do Brasileirão 2025: {times}')
print('-=' * 30)
print(f'Os 5 primeiros são: {times[0:5]}')
print('-=' * 30)
print(f'Os últimos 4 colocados são: {times[-4:]}')
print('-=' * 30)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 30)
print(f'O Internacional está na {times.index('Internacional') + 1}ª posição.')