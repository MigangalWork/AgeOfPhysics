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
        """
        if pygame.display.get_init():

            pygame.display.quit()
        """            
        
        pygame.display.init()
        self.pantallita = pygame.display.set_mode(self.screen_size, pygame.HWSURFACE)
        print("Pantalla Creada")
        print(self.pantallita)

        #self.image()

                
    def maps(self, map_size):

        self.supmapa = pygame.Surface(map_size, pygame.HWSURFACE)
        print(self.supmapa)
        self.supmapaAir = pygame.Surface(map_size, pygame.HWSURFACE)
        self.supmapaSpace = pygame.Surface(map_size, pygame.HWSURFACE)
        self.pantallita.blit(self.supmapa, (0,0))

    def image(self):

        for key1 in self.images:
            for key2 in self.images[key1]:
                for key3 in self.images[key1][key2]:
                    num = 0
                    for key4 in self.images[key1][key2][key3]:
                        
                        self.images[key1][key2][key3][key4] = pygame.image.fromstring(self.images[key1][key2][key3][key4], (int(list(self.images[key1][key2][key3].keys())[num]), int(list(self.images[key1][key2][key3].keys())[num])), 'RGB')
                       
                        num = num + 1
                        
    def displayCreate(self, mapaActual, map_generator, movex, movey, zoomv, supmapa, map_size):

        mapa = mapaActual.create(map_generator.map_list, self.images, movex, movey, zoomv, map_size)
        self.supmapa = pygame.image.fromstring(mapa, map_size, 'RGB')

    def display(self, mapaActual, map_generator, movex, movey, zoomv, supmapa, map_size):
        
        self.pantallita.fill(self.screen_filled_color)
        self.pantallita.blit(self.supmapa, (0 + movex, 0 + movey))


    
    def returnScreen(self):
        return self.pantallita

    def returnMaps(self):
        return self.supmapa, self.supmapaAir, self.supmapaSpace

    def screenSize(self, width, heigth, screen_size, variables):

        self.screen_size = (width, height)
        variables['screen_size'] = self.screen_size
        self.screen()

