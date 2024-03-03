import pygame
import Player1
import Player2
import Wall

PL1 = Player1.Player1(370, 700, 30, 50, 10, "Player1.png")
PL2 = Player2.Player2(370, 100, 30, 50, 10, "Player2.png")
Walls = Wall.Walls(0, 30, 800, 800, "Walls.png")



window = pygame.display.set_mode((800, 800))
fps = pygame.time.Clock()

game = True
while game:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
            pygame.quit()

    window.fill((204, 204, 255))
    PL1.render(window)
    PL1.move()
    if PL1.hit_box.x < -50:
        PL1.hit_box.x = 800
    if PL1.hit_box.x > 800:
        PL1.hit_box.x = -50
    if PL1.hit_box.y < 0:
        PL1.hit_box.y = 800
    if PL1.hit_box.y < 0:
        PL1.hit_box.y = 500
    PL2.render(window)
    PL2.move()
    if PL2.hit_box.x < -50:
        PL2.hit_box.x = 800
    if PL2.hit_box.x > 800:
        PL2.hit_box.x = -50
    if PL2.hit_box.y > 800:
        PL2.hit_box.y = 0
    if PL2.hit_box.y < 0:
        PL2.hit_box.y = 800



    Walls.render(window)

    for B in PL1.bulles:
        B.render(window)
        B.move()
        if B.hit_box.colliderect(PL2.hit_box):
            game = False


    for B in PL2.bulles:
        B.render(window)
        B.move()
        if B.hit_box.colliderect(PL1.hit_box):
            game = False


    pygame.display.flip()
    fps.tick(60)
