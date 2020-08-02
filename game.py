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

# chose whether rectangle or circle
draw_object = 'rect'
first_open = True
second_open = True
third_open = True
fourth_open = True
fifth_open = True
sixth_open = True
seventh_open = True
eighth_open = True
ninth_open = True
# game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if first.collidepoint(pos) and fifth_open:
                if draw_object == "rect":
                    pygame.draw.rect(screen, (225, 0, 0), (62, 38, 75, 75))
                    draw_object = 'circle'
                else:
                    pygame.draw.circle(screen, (0, 225, 0), (100, 75), 37)
                    draw_object = "rect"
                first_open = False
            if second.collidepoint(pos) and second_open:
                if draw_object == "rect":
                    pygame.draw.rect(screen, (225, 0, 0), (187, 38, 75, 75))
                    draw_object = 'circle'
                else:
                    pygame.draw.circle(screen, (0, 225, 0), (225, 75), 37)
                    draw_object = "rect"
                second_open = False
            if third.collidepoint(pos) and third_open:
                if draw_object == "rect":
                    pygame.draw.rect(screen, (225, 0, 0), (312, 38, 75, 75))
                    draw_object = 'circle'
                else:
                    pygame.draw.circle(screen, (0, 225, 0), (350, 75), 37)
                    draw_object = "rect"
                third_open = False

            if fourth.collidepoint(pos) and fourth_open:
                if draw_object == "rect":
                    pygame.draw.rect(screen, (225, 0, 0), (62, 163, 75, 75))
                    draw_object = "circle"
                else:
                    pygame.draw.circle(screen, (0, 225, 0), (100, 200), 37)
                    draw_object = "rect"
                fourth_open = False
            if fifth.collidepoint(pos) and fifth_open:
                if draw_object == "rect":
                    pygame.draw.rect(screen, (225, 0, 0), (187, 163, 75, 75))
                    draw_object = "circle"
                else:
                    pygame.draw.circle(screen, (0, 225, 0), (225, 200), 37)
                    draw_object = "rect"
                fifth_open = False
            if sixth.collidepoint(pos) and sixth_open:
                if draw_object == "rect":
                    pygame.draw.rect(screen, (225, 0, 0), (312, 163, 75, 75))
                    draw_object = "circle"
                else:
                    pygame.draw.circle(screen, (0, 225, 0), (350, 200), 37)
                    draw_object = "rect"
                sixth_open = False

            if seventh.collidepoint(pos) and seventh_open:
                if draw_object == "rect":
                    pygame.draw.rect(screen, (225, 0, 0), (62, 288, 75, 75))
                    draw_object = "circle"
                else:
                    pygame.draw.circle(screen, (0, 225, 0), (100, 325), 37)
                    draw_object = "rect"
                seventh_open = False
            if eighth.collidepoint(pos) and eighth_open:
                if draw_object == "rect":
                    pygame.draw.rect(screen, (225, 0, 0), (187, 288, 75, 75))
                    draw_object = "circle"
                else:
                    pygame.draw.circle(screen, (0, 225, 0), (225, 325), 37)
                    draw_object = "rect"
                eighth_open = False
            if ninth.collidepoint(pos) and ninth_open:
                if draw_object == "rect":
                    pygame.draw.rect(screen, (225, 0, 0), (312, 288, 75, 75))
                    draw_object = "circle"
                else:
                    pygame.draw.circle(screen, (0, 225, 0), (350, 325), 37)
                    draw_object = "rect"
                ninth_open = False

    pygame.display.update()
pygame.quit()
