import pygame

pygame.init()

screen = pygame.display.set_mode((1280, 720))

pygame.display.set_caption("Bubble Buster")
icon = pygame.image.load('NDTC.png')
pygame.display.set_icon(icon)

# Background image
background = pygame.image.load('bg.png')

# Player images for walking animation
walk_images = [pygame.image.load('Walk1.png'),
               pygame.image.load('Walk2.png'),
               pygame.image.load('Walk3.png'),
               pygame.image.load('Walk4.png')]


static_image_left = pygame.image.load('Walk1.png')


player_index = 0
playerImg = walk_images[player_index]
playerX = 660
playerY = 628
playerX_change = 0
playerY_change = 0
is_facing_left = False

def player(x, y):
    screen.blit(playerImg, (x, y))

# Animation settings
frame_counter = 0
animation_speed = 10

# Game loop
running = True
clock = pygame.time.Clock()  # Clock to control the frame rate
while running:
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

#Pag clinick ang A,D or Left Right na arrow
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                playerX_change = -2.5
                player_index = 1
                is_facing_left = True
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                playerX_change = 2.5
                player_index = 3
                is_facing_left = False

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
                player_index = 0

#Naaga lakad na animation
    if playerX_change != 0:
        playerImg = walk_images[player_index]
        if is_facing_left:
            playerImg = pygame.transform.flip(playerImg, True, False)
    else:
        playerImg = static_image_left if is_facing_left else walk_images[0]

    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 1216:
        playerX = 1216

    player(playerX, playerY)
    pygame.display.update()


    frame_counter += 1
    if frame_counter >= animation_speed:
        frame_counter = 0
        if playerX_change != 0:
            player_index += 1
            if player_index >= len(walk_images):
                player_index = 0

    clock.tick(60)

pygame.quit()
