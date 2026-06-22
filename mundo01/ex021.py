import pygame
import time

# Para o exercício do Guanabara, o código original pode funcionar, mas às vezes o áudio toca muito rápido ou o programa fecha antes de você perceber.

pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()

while pygame.mixer.music.get_busy():
    time.sleep(0.1)

pygame.quit()