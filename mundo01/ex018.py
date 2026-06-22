from math import radians, sin, cos, tan

angulo_graus = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(angulo_graus))
cosseno = cos(radians(angulo_graus))
tangente = tan(radians(angulo_graus))

print(f'O ângulo de {angulo_graus:.1f} tem o SENO de {seno:.2f}\n'
      f'O ângulo de {angulo_graus:.1f} tem o COSSENO de {cosseno:.2f}\n'
      f'O ângulo de {angulo_graus:.1f} tem a TANGENTE de {tangente:.2f}')