import pygame, sys
import ctypes

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

fps = 60

run = True
white = (255,255,255)
negro = (0,0,0)
movex = 0
movey = 0

class game:

    def play():

        global run, move
        
        while run : 

            #Pintamos la pantalla
            pantallita.fill(white)
            pygame.draw.rect(pantallita, (0,0,0), (300 + movex,300 + movey,4,40))

            #Vemos si el raton esta en algun borde para mover el mapa
            border.check(pygame.mouse.get_pos())
            

            for event in pygame.event.get():

                if event.type == pygame.QUIT:

                    pygame.quit()
                    sys.exit()
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(pygame.mouse.get_pos()[0])
                    xy = pygame.mouse.get_pos()
                    click = raton(pygame.mouse.get_pos(), 1)
                    click.click()
                    
                if event.type == pygame.KEYDOWN:
                    print(event.key)
                    if event.key == pygame.K_a: 
                        print ("holaholita")
                        #move -= 10
                    tecla2 = tecla(event.key)
                    tecla2.move()

            clock.tick(fps)
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
            movex += 1
        if m[0] <= 20:
            movex -= 1
        if m[1] >= screen_size[1]-20:
            movey += 1
        if m[1] <= 20:
            movey -= 1


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

game.play()