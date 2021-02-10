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

screen_size = (1920,1080)

pantallita = pygame.display.set_mode( screen_size )

class game:

    def play():

        global run, move, zoomv, mapaactual
        
        while run : 

            #Pintamos la pantalla
            pantallita.fill(white)
            
            mapaactual.create() 
            
            pygame.draw.rect(pantallita, (0,0,0), (300 + movex, 300 + movey, 4 + sizex, 40 + sizey))
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

                    print(event)
                    print(event.y)
                    mapaactual = zoom.zoom(event.y)
                    

                if event.type == pygame.KEYDOWN:
                    print(event.key)
                    if event.key == pygame.K_a: 
                        print ("holaholita")
                        #move -= 10
                    tecla2 = tecla(event.key)
                    tecla2.move()

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
            movex -= 1
        if m[0] <= 20:
            movex += 1
        if m[1] >= screen_size[1]-20:
            movey -= 1
        if m[1] <= 20:
            movey += 1


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
class test:
    def __init__ (self, num, texto):
        self.num = num
        self.texto = texto
        self.p = "pipa"

class generador:
    def __init__(self,evento):
        self.tamano
        self.cuadrado

class intext:

    def __init__(self,evento):
        self.evento = evento


class zoom:

    def zoom(evento):
        global zoomv, mapaactual
        if evento < 5:
            zoomv = zoomv + evento * 5
            if zoomv < 5:
                zoomv = 5
            mapaactual = mapa(zoomv)
            print(zoomv)
            print("hola")
            return mapaactual
        return mapaactual    



class mapa:

    def __init__(self, imgsize):
        self.imgsize = imgsize
        self.imagen = ("images/image1.png", "images/image2.png")
        self.base_image = pygame.image.load(self.imagen[0])
        self.base_image2 = pygame.image.load(self.imagen[1])
        self.resize1 = mapa.sizemap(self.imgsize, self.base_image)
        self.resize2 = mapa.sizemap(self.imgsize, self.base_image2)

    def create(self):
        resize = (self.resize1, self.resize2)
        for i in range (0 + movex,192 +movex):
            for j in range (0 + movey ,108 +  movey):
                pantallita.blit(resize[random.randint(0,1)],(i*self.imgsize,j*self.imgsize))

    def sizemap(imgsize, base_image):
        
        red_image = pygame.transform.scale(base_image, (imgsize, imgsize))
        return red_image


mapaactual = mapa(50)

mapaactual.create()        
game.play()
