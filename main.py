import pygame
import Player1
import Player2
from Wall import Wall
import time


def start_game():

    def emd_Game(window, text):
        fps = pygame.time.Clock()
        game = True
        while game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False
                    pygame.quit()

                keys = pygame.key.get_pressed()
                if keys[pygame.K_ESCAPE]:
                    pygame.quit()
                    return

            window.blit(text, (200,400))
            pygame.display.flip()
            fps.tick(60)

    pygame.init()
    pygame.font.init()

    PL1 = Player1.Player1(370, 600, 30, 50, 10, "Player1.png")
    PL2 = Player2.Player2(370, 70, 30, 50, 10, "Player2.png")

    start_time = time.time()
    Curent_time = pygame.font.SysFont(None, 20).render("Час:",True, (0,0,0))
    PL1_win = pygame.font.SysFont(None, 100).render("Player1 WIN",True, (0,0,0))
    PL2_win = pygame.font.SysFont(None, 100).render("Player2 WIN",True, (0,0,0))

    window = pygame.display.set_mode((800, 800))
    fps = pygame.time.Clock()



    walls = []
    walls.append(Wall(40, 130, 20, 160,(255, 255, 0)))
    walls.append(Wall(310, 190, 20, 160, (255, 255, 0)))
    walls.append(Wall(600, 130, 20, 160, (255, 255, 0)))

    walls.append(Wall(40, 600, 20, 160,(255, 255, 0)))
    walls.append(Wall(310, 520, 20, 160, (255, 255, 0)))
    walls.append(Wall(600, 600, 20, 160, (255, 255, 0)))


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

        for B in PL1.bulles:
            B.render(window)
            B.move()
            if B.hit_box.colliderect(PL2.hit_box):
                game = False
                emd_Game(window,PL2_win)
                return

            for wall in walls:
                if B.hit_box.colliderect(wall.rect):
                    PL1.bulles.remove(B)

        for B in PL2.bulles:
            B.render(window)
            B.move()
            if B.hit_box.colliderect(PL1.hit_box):
                game = False
                emd_Game(window,PL1_win)
                return

            for wall in walls:
                if B.hit_box.colliderect(wall.rect):
                    PL2.bulles.remove(B)

        for wall in walls:
            wall.render(window)

        for wall in walls:
            if wall.rect.colliderect(PL1.hit_box):
                if PL1.derection == "верх":
                    PL1.hit_box.y += PL1.speed
                if PL1.derection == "вниз":
                    PL1.hit_box.y -= PL1.speed
                if PL1.derection == "вправо":
                    PL1.hit_box.x -= PL1.speed
                if PL1.derection == "вліво":
                    PL1.hit_box.x += PL1.speed

        for wall in walls:
            if wall.rect.colliderect(PL2.hit_box):
                if PL2.derection == "верх":
                    PL2.hit_box.y += PL1.speed
                if PL2.derection == "вниз":
                    PL2.hit_box.y -= PL1.speed
                if PL2.derection == "вправо":
                    PL2.hit_box.x -= PL1.speed
                if PL2.derection == "вліво":
                    PL2.hit_box.x += PL1.speed

        current_time =round(time.time() - start_time)
        Curent_time = pygame.font.SysFont(None, 30).render("Час:" + str(current_time), True, (0, 0, 0))

        window.blit(Curent_time, (20, 15))

        pygame.display.flip()
        fps.tick(60)
