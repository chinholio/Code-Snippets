import pygame
from sys import exit

# starts pygame
pygame.init()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('Python/PyGame Runner/font/Pixeltype.ttf', 50)


sky_surface = pygame.image.load('Python/PyGame Runner/graphics/Sky.png')
ground_surface = pygame.image.load('Python/PyGame Runner/graphics/ground.png')
text_surface = test_font.render('My game', False, 'Black')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    screen.blit(text_surface,(300,50))
 
    # draw all elements
    # update everything
    pygame.display.update()
    # Sets maximum frame rate
    clock.tick(60)