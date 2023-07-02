import pygame
from sys import exit

pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill('red')
        self.rect = self.image.get_rect(center=(400, 300))
        self.speed = 5
        self.yvel = 0
        self.falling = False

    def gravity(self):
        self.yvel += gravity
        self.rect.y += self.yvel

    def render(self):
        screen.blit(self.image, self.rect)

    def falling_check(self):
        if self.rect.bottom >= 600:
            self.yvel = 0
            self.rect.bottom = 600
            self.falling = False

    # def apex(self):
    #     while self.yvel > 0:
    #         pass
    #     self.yvel = 0
    #     self.rect.x += self.speed
    #     self.falling_check()

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.falling == False:
            self.yvel = -15
            self.falling = True

        self.gravity()
        self.falling_check()
        self.render()

player = Player()
gravity = 0.5

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill((255, 255, 255))
    player.update()

    pygame.display.flip()
    clock.tick(60)
