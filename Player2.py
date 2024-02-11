import pygame
class Player2:
    def __init__(self, x, y, w, h, speed, texture):
        self.speed = speed
        self.texture = pygame.image.load(texture)
        self.texture = pygame.transform.scale(self.texture, (w, h))
        self.hit_box = self.texture.get_rect()
        self.hit_box.x = x
        self.hit_box.y = y


    def render(self, window):
        window.blit(self.texture, (self.hit_box.x, self.hit_box.y))


    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_l]:
            self.hit_box.x += self.speed
        if keys[pygame.K_j]:
            self.hit_box.x -= self.speed
        if keys[pygame.K_i]:
            self.hit_box.y += self.speed
        if keys[pygame.K_l]:
            self.hit_box.y -= self.speed

