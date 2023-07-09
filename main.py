import pygame
from sys import exit

pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

gravity = 0.5

class Entity(pygame.sprite.Sprite):
    def __init__(self, color, speed, jumpHeight):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=(400, 300))
        self.speed = speed
        self.jumpHeight = jumpHeight
        self.yvel = 0
        self.falling = True
        self.direction = 1
        self.xvel = 0

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

    def friction(self, x):
        self.xvel *= x

    def movement(self):
        self.rect.x += self.xvel
        self.rect.y += self.yvel
        self.friction(0.8)

    def update(self):
        self.movement()
        self.falling_check()
        self.render()
        if self.falling:
            self.gravity()

    def jump(self):
        if not self.falling:
            self.yvel += -self.jumpHeight
            self.falling = True

class Player(Entity):
    def __init__(self, color, speed, jumpHeight, dashSpeed):
        super().__init__(color, speed, jumpHeight)
        self.dashSpeed = dashSpeed
        self.cooldown = 0
        self.original_color = color
        self.current_color = color

    def update(self):
        super().update()
        if self.cooldown > 0:
            self.cooldown -= 1

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.xvel -= self.speed
            self.direction = -1
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.xvel += self.speed
            self.direction = 1

        if keys[pygame.K_x] and self.cooldown <= 0:
            self.cooldown = 60  # Cooldown for 1 second (assuming 60 FPS)
            self.xvel += self.dashSpeed * self.direction
            self.current_color = (255, 255, 255)  # Change to white during dash

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.jump()

        if not keys[pygame.K_x] and self.current_color != self.original_color:
            self.current_color = self.original_color  # Revert to original color after dash

        self.image.fill(self.current_color)


player = Player((255, 0, 0), 2, 10, 50)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill((192, 192, 192))
    player.update()

    pygame.display.flip()
    clock.tick(60)
