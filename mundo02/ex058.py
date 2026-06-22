from random import randint
num_computador = randint(0, 10)
print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
acertou = False
tentativas = 0
while not acertou:
    num_jogador = int(input('Qual é seu palpite? '))
    tentativas += 1
    if num_jogador == num_computador:
        acertou = True
    else:
        if num_jogador < num_computador:
            print('Mais... Tente mais uma vez.')
        elif num_jogador > num_computador:
            print('Menos... Tente mais uma vez.')
print(f'Acertou com {tentativas} tentativas. Parabéns!')
