import pygame
import random

# initialize game
pygame.init()
# determine the screen display size for the game
screen = pygame.display.set_mode((1280, 720))
# Parameters for Player
playerW = 50
playerH = 50
playerX = 300
playerY = 250

# Parameters for Food spawning
eaten = True
foodX = random.randrange(1280)
foodY = random.randrange(720)

# Tracking the number of total collected fruit with "score"
score = 0
# Load the font
myfont = pygame.font.Font('SourceSansPro-Bold.otf', size=70)


while True:

    # Refresh screen at the start of each loop
    screen.fill('black')

    # if the food was eaten, the Coordinates will change
    if (eaten):
        foodX = random.randrange(1280)
        foodY = random.randrange(720)
        eaten = False

    key = pygame.key.get_pressed()

    # Process player inputs - WASD
    if key[pygame.K_a]:
        # moving left
        playerX -= 1    # move_ip = "move in place"
    elif key[pygame.K_d]:
        # moving right
        playerX += 1
    elif key[pygame.K_w]:
        # moving up
        playerY -= 1
    elif key[pygame.K_s]:
        # moving down
        playerY += 1

    # draw the food
    food = pygame.Rect(foodX, foodY, 15, 15)
    pygame.draw.rect(screen, "yellow", food)

    # draw the player
    player = pygame.Rect(playerX, playerY, playerW, playerH)
    pygame.draw.rect(screen, (255, 0, 0), player)

    # if collision occurs: the food will be eaten
    # and the size of the player gets bigger
    # and the score increases by 1
    if (player.colliderect(food)):
        eaten = True
        playerW += 20
        playerH += 20
        score += 1

    # Render, Update and display the current score
    text = myfont.render("Score: "+str(score), True, 'white')
    screen.blit(text, (980, 0))

    # Event-loop for quitting the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
    # Refresh on-screen display
    pygame.display.flip()  # Refresh on-screen display
