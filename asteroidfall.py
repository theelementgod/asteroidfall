import pygame
import random

pygame.init()

screen_width, screen_height = 640, 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('AstroidFall')

astronaut_original = pygame.transform.scale(pygame.image.load('./assets/astronaut.png'),(100,100))
asteroid = pygame.transform.scale(pygame.image.load('./assets/asteroid.png'),(50,50))

astronaut_size = astronaut_original.get_size()
astronaut_pos = [screen_width//2 , screen_height - astronaut_size[1]]
astronaut = astronaut_original.copy()
facing_right = False

asteroid_size = asteroid.get_size()
asteroid_pos = [random.randint(0, screen_width - asteroid_size[0]) , 0]
asteroid_speed = 5

clock = pygame.time.Clock()
game_over = False

speed_clock = 0

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    if speed_clock%50==0:
        asteroid_speed += 1

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        astronaut_pos[0] -= 10
        if facing_right:
            astronaut = pygame.transorm.flip(astronaut, True, False)
            facing_right = False
    elif keys[pygame.K_RIGHT]:
        asteroid_pos[0] += 10
        if not facing_right:
            asteroid = pygame.transorm.flip(astronaut, True, False)
            facing_right = True

    astronaut_pos[0] = max(0, min(asteroid_pos[0], screen_width - astronaut_size[0]))

    asteroid_pos[1] += asteroid_speed

    asteroid_pos[1] += asteroid_speed
    if asteroid_pos[1] > screen_height:
        asteroid_pos = [random.randint(0, screen_width - asteroid_size[1])]

    astronaut_rect = pygame.Rect(astronaut_pos[0], astronaut_pos[1], astronaut_size[0], astronaut_size[1])
    asteroid_rect = pygame.Rect(asteroid_pos[0], asteroid_pos[1], asteroid_size[0], asteroid_size[1])
    if astronaut_rect.colliderect(asteroid_rect):
        game_over = True

    screen.fill((0,0,0))
    screen.blit(astronaut, (astronaut_pos[0], astronaut_pos[1]))
    screen.blit(asteroid, (asteroid_pos[0], asteroid_pos[1]))
    pygame.display.update()

    speed_clock += 1

    clock.tick(30)

pygame.quit()

# Kevin Beier