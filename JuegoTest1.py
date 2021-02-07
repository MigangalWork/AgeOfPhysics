import pygame

pygame.init()

clock = pygame.time.Clock()

screen_size = (400,400)

pantallita = pygame.display.set_mode( screen_size )

fps = 60

run = True
white = (255,255,255)
negro = (0,0,0)

while run : 

    pantallita.fill(white)
    pygame.draw.rect(pantallita, (0,0,0), (300,0,4,40))

    background = [white, white, white, white, white, white]
    screen = create_graphics_screen()
    for i in range(6):
        screen.blit(background[i], (i*10, 0))
    playerpos = 3
    screen.blit(negro, (playerpos*10, 0))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            pygame.quit()
            run = False
            
    pygame.display.update()        