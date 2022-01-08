import pygame
pygame.init()
pygame.mixer.music.load('Exercicio_21.mp3')
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play()
input()
pygame.event.wait()