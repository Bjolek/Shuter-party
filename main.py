
import pygame


window = pygame.display.set_mode((800, 500))
fps = pygame.time.Clock()


while True:

    pygame.display.flip()
    fps.tick(60)