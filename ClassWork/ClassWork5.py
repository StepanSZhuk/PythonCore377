import pygame
''' Home work. Написати код анімації квадрата, який переміщається від лівої межі до правої,
 дотикається до неї, але не зникає за нею.
 Після цього повертається назад – від правої межі до лівої, дотикається до неї, і знову рухається вправо. 
 Цикли руху квадрата повторюються до завершення програми.'''

pygame.init()
gameDisplay=pygame.display.set_mode((700,500))
pygame.display.set_caption("Home work")

WHITE = (255,255,255)
BLACK = (0,0,0)

square_x =0
square_y =50
 
square_change_x=10
# square_change_y=10

run=True

clock = pygame.time.Clock()

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    square_x += square_change_x
    # square_y += square_change_y

    # if square_y>450 or square_y<0:
    #     square_change_y *= -1
    if square_x > 650 or square_x < 0:
        square_change_x *= -1

    gameDisplay.fill(BLACK)   
    pygame.draw.rect(gameDisplay, WHITE, [square_x, square_y, 50, 50])
    clock.tick(60)
    pygame.display.update()
pygame.quit()
