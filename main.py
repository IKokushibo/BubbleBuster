import pygame

pygame.init()

screen = pygame.display.set_mode((1280, 720))

pygame.display.set_caption("Bubble Buster")
icon = pygame.image.load('NDTC.png')
pygame.display.set_icon(icon)

#background image
background = pygame.image.load('bg.png')


#player

playerImg = pygame.image.load('Walk1.png')
playerX = 660
playerY =660
playerX_change = 0

def player(x, y):
def player(x, y):
    screen.blit(playerImg, (playerX, playerY))

#game loop


running = True
while running:
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    player(playerX, playerY)
    pygame.display.update()

pygame.quit()
