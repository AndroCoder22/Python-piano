import pygame

import sound
import notes

pygame.init()
sc = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

sound_lines = {}
keys = "/.,mnbvcxz';lkjhgfdsa][poiuytrewq"

while True:
    clock.tick(100)
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            exit()
        if ev.type == pygame.KEYDOWN:
            sound_lines.update({str(ev.unicode): {"sound": sound.sound(0.1, str(ev.unicode))}})
        if ev.type == pygame.KEYUP:
            sound_lines[str(ev.unicode)]["sound"].stop()
