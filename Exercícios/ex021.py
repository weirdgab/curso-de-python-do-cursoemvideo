import pygame
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(
    '/home/weirdgab/Scripts/Curso Python/Exercícios/ex021.mp3')
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)

pygame.event.wait()
