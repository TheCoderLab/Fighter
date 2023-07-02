import pygame
from sys import exit

pygame.init()

# Define screen dimensions
screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Fighting Game')
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill('red')
        self.rect = self.image.get_rect(center=(200, 300))
        self.speed = 5
        self.yvel = 0
        self.falling = False

    def gravity(self):
        self.yvel += gravity
        self.rect.y += self.yvel

    def render(self):
        screen.blit(self.image, self.rect.move(-camera_x, 0))

    def falling_check(self):
        if self.rect.bottom >= 600:
            self.yvel = 0
            self.rect.bottom = 600
            self.falling = False

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and not self.falling:
            self.yvel = -15
            self.falling = True

        self.gravity()
        self.falling_check()
        self.render()

player = Player()
gravity = 0.5

world_width = 1600
world_height = 1200

camera_x = 0
camera_velocity = 0
camera_damping = 0.1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Update camera position based on player position
    target_camera_x = player.rect.x - screen_width // 2
    camera_velocity = (target_camera_x - camera_x) * camera_damping
    camera_x += camera_velocity

    # Keep camera within the game world boundaries
    camera_x = max(0, min(camera_x, world_width - screen_width))

    screen.fill((255, 255, 255))
    player.update()

    pygame.display.flip()
    clock.tick(60)
