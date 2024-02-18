import pygame
import Player1
import Player2



PL1 = Player1.Player1(0, 700, 30, 50, 10, "Player1.png")
PL2 = Player2.Player2(0, 100, 30, 50, 10, "Player2.png")



window = pygame.display.set_mode((800, 800))
fps = pygame.time.Clock()

game = True
while game:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
            pygame.quit()
    window.fill((204,204,255))
    PL1.render(window)
    PL1.move()
    PL2.render(window)
    PL2.move()
    pygame.display.flip()
    fps.tick(60)