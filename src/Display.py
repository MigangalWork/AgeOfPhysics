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
        pantallita = pygame.display.set_mode(screen_size)
        self.pantallita = pantallita
        
        
    def maps(self, map_size):

        self.supmapa = pygame.Surface(map_size)
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