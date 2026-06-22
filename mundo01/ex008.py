distancia = float(input('Digite uma distância em metros: '))

print(f'A medida de {distancia:.1f}m corresponde a\n'
      f'{distancia / 1000}km\n'
      f'{distancia / 100}hm\n'
      f'{distancia / 10}dam\n'
      f'{distancia * 10:.0f}dm\n'
      f'{distancia * 100:.0f}cm\n'
      f'{distancia * 1000:.0f}mm')