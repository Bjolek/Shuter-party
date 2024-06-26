import pygame
import Bullet
import time


class Player:
    def __init__(self, x, y, w, h, speed, texture, K_UO, K_Down, K_Left, K_Right, K_Shoot, ShootDirection):
        self.speed = speed
        self.texture = pygame.image.load(texture)
        self.texture = pygame.transform.scale(self.texture,(w, h ))
        self.hit_box = self.texture.get_rect()
        self.hit_box.x = x
        self.hit_box.y = y
        self.bulles = []
        self.last_shot_time = time.time()
        self.derection = ("вгору")
        self.K_UO = K_UO
        self.K_Down = K_Down
        self.K_Left = K_Left
        self.K_Right = K_Right
        self.K_Shoot = K_Shoot
        self.ShootDirection = ShootDirection

    def render (self, window):
        window.blit(self.texture, (self.hit_box.x, self.hit_box.y))
        for b in self.bulles:
            b.render(window)

    def bullet_time_to_shot(self):
        current_time = time.time()
        if current_time - self.last_shot_time >= 0.3:
            self.last_shot_time = current_time
            return True
        else:
            return False

    def move(self):
        for d in self.bulles:
            d.move()
        keys = pygame.key.get_pressed()


        if keys[self.K_Right]:
            self.hit_box.x += self.speed
            self.derection="вправо"
        if keys[self.K_Left]:
            self.hit_box.x -= self.speed
            self.derection = "вліво"
        if keys[self.K_UO]:
            self.hit_box.y -= self.speed
            self.derection = "верх"
        if keys[self.K_Down]:
            self.derection = "вниз"
            self.hit_box.y += self.speed
        if keys[self.K_Shoot] and self.bullet_time_to_shot():
            self.bulles.append(Bullet.Bullet(self.hit_box.x, self.hit_box.y, 7 ,20, 5 if self.ShootDirection == True else -5, "bullet.png"))




