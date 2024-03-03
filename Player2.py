import pygame
import Bullet
import time

class Player2:
    def __init__(self, x, y, w, h, speed, texture):
        self.speed = speed
        self.texture = pygame.image.load(texture)
        self.texture = pygame.transform.scale(self.texture, (w, h))
        self.hit_box = self.texture.get_rect()
        self.hit_box.x = x
        self.hit_box.y = y
        self.bulles = []
        self.last_shot_time = time.time()

    def bullet_time_to_shot(self):
        current_time = time.time()
        if current_time - self.last_shot_time >= 0.3:
            self.last_shot_time = current_time
            return True
        else:
            return False

    def render(self, window):
        window.blit(self.texture, (self.hit_box.x, self.hit_box.y))
        for b in self.bulles:
            b.render(window)

    def move(self):
        for d in self.bulles:
            d.move()
        keys = pygame.key.get_pressed()

        if keys[pygame.K_l]:
            self.hit_box.x += self.speed
        if keys[pygame.K_j]:
            self.hit_box.x -= self.speed
        if keys[pygame.K_i]:
            self.hit_box.y -= self.speed
        if keys[pygame.K_k]:
            self.hit_box.y += self.speed
        if keys[pygame.K_n] and self.bullet_time_to_shot():
            self.bulles.append(Bullet.Bullet(self.hit_box.x, self.hit_box.y, 7, 20, -5, "bullet.png"))
