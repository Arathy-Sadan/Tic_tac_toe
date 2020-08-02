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
first = pygame.draw.rect(screen, (225, 225, 225), (50, 25, 100, 100))
second = pygame.draw.rect(screen, (225, 225, 225), (175, 25, 100, 100))
third = pygame.draw.rect(screen, (225, 225, 225), (300, 25, 100, 100))

fourth = pygame.draw.rect(screen, (225, 225, 225), (50, 150, 100, 100))
fifth = pygame.draw.rect(screen, (225, 225, 225), (175, 150, 100, 100))
sixth = pygame.draw.rect(screen, (225, 225, 225), (300, 150, 100, 100))

seventh = pygame.draw.rect(screen, (225, 225, 225), (50, 275, 100, 100))
eighth = pygame.draw.rect(screen, (225, 225, 225), (175, 275, 100, 100))
ninth = pygame.draw.rect(screen, (225, 225, 225), (300, 275, 100, 100))

# game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if first.collidepoint(pos):
                pygame.draw.rect(screen, (225, 0, 0), (62, 38, 75, 75))
                pygame.draw.circle(screen, (0, 225, 0), (100, 75), 37)
            if second.collidepoint(pos):
                pygame.draw.rect(screen, (225, 0, 0), (187, 38, 75, 75))
                pygame.draw.circle(screen, (0, 225, 0), (225, 75), 37)
            if third.collidepoint(pos):
                pygame.draw.rect(screen, (225, 0, 0), (312, 38, 75, 75))
                pygame.draw.circle(screen, (0, 225, 0), (350, 75), 37)

            if fourth.collidepoint(pos):
                pygame.draw.rect(screen, (225, 0, 0), (62, 163, 75, 75))
                pygame.draw.circle(screen, (0, 225, 0), (100, 200), 37)
            if fifth.collidepoint(pos):
                pygame.draw.rect(screen, (225, 0, 0), (187, 163, 75, 75))
                pygame.draw.circle(screen, (0, 225, 0), (225, 200), 37)
            if sixth.collidepoint(pos):
                pygame.draw.rect(screen, (225, 0, 0), (312, 163, 75, 75))
                pygame.draw.circle(screen, (0, 225, 0), (350, 200), 37)

            if seventh.collidepoint(pos):
                pygame.draw.rect(screen, (225, 0, 0), (62, 288, 75, 75))
                pygame.draw.circle(screen, (0, 225, 0), (100, 325), 37)
            if eighth.collidepoint(pos):
                pygame.draw.rect(screen, (225, 0, 0), (187, 288, 75, 75))
                pygame.draw.circle(screen, (0, 225, 0), (225, 325), 37)
            if ninth.collidepoint(pos):
                pygame.draw.rect(screen, (225, 0, 0), (312, 288, 75, 75))
                pygame.draw.circle(screen, (0, 225, 0), (350, 325), 37)

    pygame.display.update()
pygame.quit()
