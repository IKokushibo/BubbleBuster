import pygame
import random

pygame.init()

screen = pygame.display.set_mode((1280, 720))

pygame.display.set_caption("Bubble Buster")
icon = pygame.image.load('NDTC.png')
pygame.display.set_icon(icon)

# Background image
background = pygame.image.load('bg1.png')

# Player images for walking animation
walk_images = [pygame.image.load(f'c{i}.png') for i in range(1, 11)]

# Static player image facing left
static_image_left = pygame.image.load('c1.png')  # Assuming the first image is the static pose

# Initial player settings
player_index = 0  # Index to track the current image in the walking animation
playerImg = walk_images[player_index]
playerX = 660
playerY = 588
playerX_change = 0
playerY_change = 0
is_facing_left = False  # Flag to track the player's facing direction

enemyImg = pygame.image.load('b1.png')
enemyX = random.randint(0, 1180)
enemyY = random.randint(50, 150)
enemyX_change = 0
enemyY_change = 0.5

bulletImg = pygame.image.load('s1.png')
bulletX = 0
bulletY = 588
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


# Animation settings
frame_counter = 0
animation_speed = 10  # Lower values make animation faster

# Game loop
running = True
clock = pygame.time.Clock()  # Clock to control the frame rate
while running:
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # If keystroke is pressed, check whether it's right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                playerX_change = -2.5
                player_index = 1  # Change index for walking animation
                is_facing_left = True  # Set the flag for facing left
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                playerX_change = 2.5
                player_index = 3  # Change index for walking animation
                is_facing_left = False  # Reset the flag for facing left
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
                player_index = 0  # Reset index for standing pose

    # Update player image based on the walking animation or static pose
    if playerX_change != 0:
        playerImg = walk_images[player_index]
        if is_facing_left:  # Flip image if facing left
            playerImg = pygame.transform.flip(playerImg, True, False)
    else:
        playerImg = static_image_left if is_facing_left else walk_images[0]

    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 1180:
        playerX = 1180

    enemyY += enemyY_change

    if enemyY >= 720:
        enemyY = random.randint(50, 150)

    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    if bulletY <= 0:
        bulletY = 588
        bullet_state = "ready"



    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()

    # Control the frame rate for smoother animation
    frame_counter += 1
    if frame_counter >= animation_speed:
        frame_counter = 0
        if playerX_change != 0:
            player_index += 1
            if player_index >= len(walk_images):
                player_index = 0

    clock.tick(60)

pygame.quit()
