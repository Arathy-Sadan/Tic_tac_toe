import pygame

# initialize pygame
pygame.init()

# screen
screen = pygame.display.set_mode((500, 500))

# logo & tittle
tittle = pygame.display.set_caption("TIC TAC TOE")
logo = pygame.image.load('tictactoe.png')
pygame.display.set_icon(logo)

# boxes
first = pygame.draw.rect(screen, (225, 225, 225), (25, 25, 100, 100))
second = pygame.draw.rect(screen, (225, 225, 225), (150, 25, 100, 100))
third = pygame.draw.rect(screen, (225, 225, 225), (275, 25, 100, 100))
four = pygame.draw.rect(screen, (225, 225, 225), (25, 150, 100, 100))
five = pygame.draw.rect(screen, (225, 225, 225), (150, 150, 100, 100))
six = pygame.draw.rect(screen, (225, 225, 225), (275, 150, 100, 100))
seven = pygame.draw.rect(screen, (225, 225, 225), (25, 275, 100, 100))
eight = pygame.draw.rect(screen, (225, 225, 225), (150, 275, 100, 100))
nine = pygame.draw.rect(screen, (225, 225, 225), (275, 275, 100, 100))
# game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
pygame.quit()
