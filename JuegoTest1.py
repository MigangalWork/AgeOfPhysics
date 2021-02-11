import pygame, sys, random
import ctypes
from VariablesGlobales import *

# This fix the monitor scaling different from 100%
# Source: https://stackoverflow.com/questions/62775254/why-does-my-pygame-window-not-fit-in-my-4k3840x2160-monitor-scale-of-pygame-w
if sys.platform == 'win32':
    # On Windows, the monitor scaling can be set to something besides normal 100%.
    # PyScreeze and Pillow needs to account for this to make accurate screenshots.
    # TODO - How does macOS and Linux handle monitor scaling?
    import ctypes
    try:
       ctypes.windll.user32.SetProcessDPIAware()
    except AttributeError:
        pass # Windows XP doesn't support monitor scaling, so just do nothing.

pygame.init()

clock = pygame.time.Clock()
ejeCoordenadas = [0,0]


pantallita = pygame.display.set_mode( screen_size )
supmapa = pygame.Surface(screen_size)
pantallita.blit(supmapa, (0,0))

class game:

    def play():

        global run, move, zoomv, movex, movey, ejeCoordenadas
        
        while run : 

            #Pintamos la pantalla
            pantallita.fill(white)
            pantallita.blit(supmapa, (0 + movex, 0 + movey))
            supmapa.fill(white)
            mapaactual.create() 
            ejeCoordenadas = [screen_size[0]/2 - movex, screen_size[1]/2 - movey]
            
            pygame.draw.rect(pantallita, (0,0,0), (ejeCoordenadas[0], ejeCoordenadas[1], 4, 40))
            #Vemos si el raton esta en algun borde para mover el mapa
            border.check(pygame.mouse.get_pos())
            
            #Miramos que eventos ocurren
            for event in pygame.event.get():

                #Miramos si se pulsa la X, de ser asi cerramos el juego
                if event.type == pygame.QUIT:

                    pygame.quit()
                    sys.exit()
                    run = False

                 #Miramos si se pulsa la un boton del raton
                if event.type == pygame.MOUSEBUTTONDOWN:
                    

                    #
                    
                    
                    #Obtenemos la posicion del raton en la pantalla y llamamos a click
                    print (pygame.MOUSEBUTTONDOWN)
                    #print(pygame.mouse.get_pos()[0])
                    xy = pygame.mouse.get_pos()
                    #click = raton(pygame.mouse.get_pos(), 1)
                    #click.click()
                    
                if event.type == pygame.MOUSEWHEEL:   
                    print (event.y)
                    zooms.zoom(event.y)
                    

                if event.type == pygame.KEYDOWN:
                    print(event.key)
                    
            
            clock.tick(60)
            pygame.display.update()        

class raton:
   

    def __init__(self, xy, num):
        self.xy = xy
        self.num = num
    
    def click(self):
        
        if self.num == 1:
            print ('Hola')

            for i in range (0, screen_size[0]+1):
                #print (i)
                objeto = test(i, "holacaracola")


class border:

    def check(m):
        global movex, movey
        if m[0] >= screen_size[0]-20:
            movex -= 5
        if m[0] <= 20:
            movex += 5
        if m[1] >= screen_size[1]-20:
            movey -= 5
        if m[1] <= 20:
            movey += 5


#class movmap:

    

class tecla:
    

    def __init__(self, num):
        self.num = num
        
    def move(self):
        global move
        if self.num == pygame.K_a:
            move -= 10
        if self.num == pygame.K_d:
            move += 10

"""
class zoom:

    def zoom(evento):
        global zoomv, mapaactual, movex, movey
        if evento < 5:
            zoomv = zoomv + evento * 5
            if zoomv < 5:
                zoomv = 5
            
            mapaactual = mapa(zoomv)
"""           
              
class zooms:

    def zoom(evento):
        global zoomv, supmapa, movex, movey, map_size, mapaactual
        
        if evento > 0 and evento < 5:
            map_size =  [int(map_size[0] * 2), int(map_size[1] * 2)]
            zoomv = int(zoomv * 2)
            print(zoomv)
            movex = movex - int(2 * ejeCoordenadas[0] - ejeCoordenadas[0])
            movey = movey - int(2 * ejeCoordenadas[1] - ejeCoordenadas[1])

        if evento < 0 and evento > -5:
            map_size =  [int(map_size[0] * 0.8), int(map_size[1] * 0.8)]
            zoomv = int(zoomv * 0.8)
            movex = movex + int(ejeCoordenadas[0] - 0.8 * ejeCoordenadas[0])
            movey = movey + int(ejeCoordenadas[1] - 0.8 * ejeCoordenadas[1])
        

        supmapa = pygame.Surface(map_size)
        supmapa.fill(white)
        mapaactual = mapa(zoomv, base_image, base_image2)
        mapaactual.create()

class mapa:

    def __init__(self, imgsize, base_image, base_image2):
        self.imgsize = imgsize
        #self.imagen = ("images/image1.png", "images/image2.png")
        #self.base_image = pygame.image.load(self.imagen[0])
        #self.base_image2 = pygame.image.load(self.imagen[1])
        self.resize1 = mapa.sizemap(self.imgsize, base_image)
        self.resize2 = mapa.sizemap(self.imgsize, base_image2)

    def create(self):
        resize = (self.resize1, self.resize2)
        for i in range (map_sizex[0], map_sizex[1]):
            for j in range (map_sizey[0], map_sizey[1]):
                supmapa.blit(resize[abs(j%2 - i%2)],(i*self.imgsize,j*self.imgsize))

    def sizemap(imgsize, base_image):
        
        red_image = pygame.transform.scale(base_image, (imgsize, imgsize))
        return red_image


mapaactual = mapa(zoomv, base_image, base_image2)

mapaactual.create()        
game.play()
