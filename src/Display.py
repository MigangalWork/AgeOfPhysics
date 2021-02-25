import pygame

class Display:
    '''
    pantallita = pygame.display.set_mode(screen_size)
    supmapa = pygame.Surface(map_size)
    supmapaAir = pygame.Surface(map_size)
    supmapaSpace = pygame.Surface(map_size)
    pantallita.blit(supmapa, (0,0))
    '''

    def __init__(self, screen_size, images, screen_filled_color):

        self.screen_size = screen_size
        self.images = images
        self.screen_filled_color = screen_filled_color
        

    def screen(self):

        if pygame.display.get_init():

            pygame.display.quit()
            
        
        pygame.display.init()
        self.pantallita = pygame.display.set_mode(self.screen_size, pygame.HWSURFACE)
        print(self.pantallita)

        return self.pantallita
                
    def maps(self, map_size):

        self.supmapa = pygame.Surface(map_size, pygame.HWSURFACE)
        print(self.supmapa)
        self.supmapaAir = pygame.Surface(map_size)
        self.supmapaSpace = pygame.Surface(map_size)
        self.pantallita.blit(self.supmapa, (0,0))

    def display(self, mapaActual, map_generator, movex, movey, zoomv, supmapa):

        self.supmapa = supmapa
        self.pantallita.fill(self.screen_filled_color)
        self.pantallita.blit(self.supmapa, (0 + movex, 0 + movey))
        self.supmapa.fill(self.screen_filled_color)
        mapaActual.create(map_generator.map_list, self.images, self.supmapa, movex, movey, zoomv, self.screen_size)
    
    def returnScreen(self):
        return self.pantallita

    def returnMaps(self):
        return self.supmapa, self.supmapaAir, self.supmapaSpace

    def screenSize(self, width, heigth, screen_size, variables):

        self.screen_size = (width, height)
        variables['screen_size'] = self.screen_size
        self.screen()

