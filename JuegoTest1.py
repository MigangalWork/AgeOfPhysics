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
supmapa = pygame.Surface(map_size)
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
            #print (ejeCoordenadas)
            pygame.draw.rect(pantallita, (0,0,0), (ejeCoordenadas[0], ejeCoordenadas[1], 4, 40))
            #Vemos si el raton esta en algun borde para mover el mapa
            border.check(pygame.mouse.get_pos(), ejeCoordenadas)
            
            #Miramos que eventos ocurren
            for event in pygame.event.get():

                #Miramos si se pulsa la X, de ser asi cerramos el juego
                if event.type == pygame.QUIT:

                    pygame.quit()
                    sys.exit()
                    run = False

                 #Miramos si se pulsa la un boton del raton
                if event.type == pygame.MOUSEBUTTONDOWN:
                    

                    xy = pygame.mouse.get_pos()
                    button = event.button

                    print (selecCasilla.posMouse(xy))
                    
                    #Obtenemos la posicion del raton en la pantalla y llamamos a click
                    #print (pygame.MOUSEBUTTONDOWN)
                    print (xy)
                    

                        
                    #print(pygame.mouse.get_pos()[0])
                    click = mouse(pygame.mouse.get_pos(), button)
                    selected = click.click()

                
                if event.type == pygame.MOUSEBUTTONUP:
                    
                    xy = pygame.mouse.get_pos()
                    click = mouse(xy, event.button)
                    selected2 = click.click()


                    if selected == selected2:
                        if selected[0][0] == -1:
                            pass
                        else:
                            if event.button == 3:
                                genMap.editMap(selected[0][0],selected[0][1],0)
                            else:
                                genMap.editMap(selected[0][0],selected[0][1],1)
                    
                    else:
                        selectedM = {}
                        casilla = 0
                        for i in range (selected[0][0], selected2[0][0]+1):
                            for j in range (selected[0][1], selected2[0][1]+1):
                                casilla = casilla + 1
                                selectedM[casilla] = [i,j]
                        print (selectedM) 
                
                    
                if event.type == pygame.MOUSEWHEEL:   
                    print (event.y)
                    zooms.zoom(event.y)
                    

                if event.type == pygame.KEYDOWN:
                    print(event.key)
                    
            
            clock.tick(60)
            pygame.display.update()        

class mouse:
   

    def __init__(self, xy, num):
        self.xy = xy
        self.num = num

    def posMouse():
        return [self.xy[0] - movex, self.xy[1] - movey]

    def click(self):
        h = {}
        if self.num == 1:
            h[0] = selecCasilla.selecCasilla(self.xy)
            print(h)
            return (h)
        else:
            return {0 : [-1,-1]}    

    def selecMulti():
        pass
        

class border:

    def check(m, eje):
        global movex, movey
        if eje[0] < map_size[0]:
            if m[0] >= screen_size[0]-20:
                movex -= 1
        if eje[0] > 0 :
            if m[0] <= 20:
                movex += 1
        if eje[1] < map_size[1]:
            if m[1] >= screen_size[1]-20:
                movey -= 1
        if eje[1] > 0 :        
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

class selecCasilla:

    def posMouse(xy):
        return [xy[0] - movex, xy[1] - movey]
    def selecCasilla(xy):
        var = -1
        var2 = -1
        x = selecCasilla.posMouse(xy)[0]
        y = selecCasilla.posMouse(xy)[1]
        for i in range (map_sizex[0], map_sizex[1]):
            for j in range (map_sizey[0], map_sizey[1]):
                if y < (j+1) * zoomv and y > (j) * zoomv :
                    var = j
                    continue
            if x < (i+1) * zoomv and x > (i) * zoomv:
                var2 = i
                continue
        if var == -1 or var2 == -1:
            return [-1,-1]
        return [var2,var]

class selecUnits:

    def selecUnits():
        var = 0
        for i in lenght(selectedM):
            if madDic[selectedM[i]] == 1:
            
                unitsSelected[var] = selectedM[i]
                var = var + 1
        print(unitsSelected)
              
class zooms:

    def zoom(evento):
        global zoomv, supmapa, movex, movey, map_size, mapaactual
        
        if evento > 0 and evento < 5:

            zoomv = int(zoomv * 2)
            
            if zoomv > 80:
                zoomv = 80
            else:
                map_size =  [map_size[0] * 2, map_size[1] * 2]
                
                movex = movex - (2 * ejeCoordenadas[0] - ejeCoordenadas[0])
                movey = movey - (2 * ejeCoordenadas[1] - ejeCoordenadas[1])

        if evento < 0 and evento > -5:
            
            zoomv = int(zoomv * 0.5)
            if zoomv < 5:
                zoomv = 5
            else:
                map_size =  [map_size[0] * 0.5, map_size[1] * 0.5]
                movex = movex - (0.5 * ejeCoordenadas[0] - ejeCoordenadas[0])
                movey = movey - (0.5 * ejeCoordenadas[1] - ejeCoordenadas[1])
        

        supmapa = pygame.Surface(map_size)
        supmapa.fill(white)
        print(zoomv)
        mapaactual = mapa(zoomv)
        mapaactual.create()


class genMap:
    
    def genMap ():
        global mapDic
        for i in range (map_sizex[0], map_sizex[1]):
            for j in range (map_sizey[0], map_sizey[1]):
                mapDic[i,j] = random.randint(0,1)
        
    def editMap(i,j,var):
        global mapDic
        global mapTile
        mapDic[i,j] = var
        mapTile[i,j]['img'] = var

class tile:

    def __init__(self, xy):
        self.xy = xy
        self.n = (xy[0],xy[1])
        self.img = mapDic[self.n]

    def tile(self):
        t = {'pos' : self.xy, 'visible' : True, 'visibleBy' : 1, 'img' : mapDic[self.n], 'unit' : False}
        return (t) 
        #pass

class tiles:

    def tiles():

        
        size = map_sizex[1] * map_sizey [1]
        for i in range (map_sizex[0], map_sizex[1]):
            for j in range (map_sizey[0], map_sizey[1]):
                t = tile([i,j])
                mapTile[i,j] = t.tile()
                


class mapa:

    def __init__(self, imgsize):
        self.imgsize = imgsize
        self.base_image = base_image
        self.resize = {}
        for i in range(len(imagen.keys())):
            self.resize[i] = mapa.sizemap(self.imgsize, base_image[i])
        


    def create(self):
        resize = (self.resize[0], self.resize[1])
        for i in range (map_sizex[0], map_sizex[1]):
            for j in range (map_sizey[0], map_sizey[1]):
                supmapa.blit(resize[mapDic[i,j]],(i*self.imgsize,j*self.imgsize))

    def sizemap(imgsize, base_image):
        
        red_image = pygame.transform.scale(base_image, (imgsize, imgsize))
        return red_image


genMap.genMap()

tiles.tiles()

mapaactual = mapa(zoomv)


mapaactual.create()        
game.play()
