import pygame, sys, random
import ctypes
from VariablesGlobales import *
from Menus import Menus

func_list = ['prueba_click("conf")', 'prueba_click("canc")']
text_list= [ 'Confirmar', 'Calcelar']
menu_prueba = Menus(200, 100, 2, func_list, text_list)

def prueba_click(text):
    print(text)

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

        global run, move, zoomv, movex, movey, ejeCoordenadas, clicking
        menu_abierto = False
        while run : 

            #Pintamos la pantalla
            pantallita.fill(white)
            pantallita.blit(supmapa, (0 + movex, 0 + movey))
            supmapa.fill(white)
            mapaactual.create() 
            ejeCoordenadas = [int(screen_size[0]/2) - movex, int(screen_size[1]/2) - movey]
            #print (ejeCoordenadas)
            if clicking[1] and selected[0]!=-1:
                pixel_selected_x = selected[0]*zoomv
                pixel_selected_y = selected[1]*zoomv
                mx, my = pygame.mouse.get_pos()

                if pixel_selected_x > mx:
                    pixel_selected_x = mx
                if pixel_selected_y > my:
                    pixel_selected_y = my
                pygame.draw.rect(pantallita, (0,0,0), (pixel_selected_x, pixel_selected_y, abs(selected[0]*zoomv - mx), abs(selected[1]*zoomv - my)))
                
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
                    
                    clicking[event.button] = True
                    # print (event.button)
                    xy = pygame.mouse.get_pos()
                    button = event.button

                    # print (selecCasilla.posMouse(xy))
                    
                    #Obtenemos la posicion del raton en la pantalla y llamamos a click
                    # print (pygame.MOUSEBUTTONDOWN)
                    # print (xy)
                    
                    
                    
                    #print(pygame.mouse.get_pos()[0])
                    click = mouse(pygame.mouse.get_pos(), button)
                    
                    
                    selected = click.click()
                    

                
                if event.type == pygame.MOUSEBUTTONUP:

                    clicking[event.button] = False

                    xy = pygame.mouse.get_pos()
                    click = mouse(xy, event.button)
                    selected2 = click.click()


                    if selected == selected2:
                        if selected[0] == -1:
                            pass
                        else:
                            if event.button == 3:
                                genMap.editMap(selected[0],selected[1],0)
                            else:
                                genMap.editMap(selected[0],selected[1],1)
                    
                    else:
                        selectedM = {}
                        casilla = 0
                        for i in range (selected[0], selected2[0]+1):
                            for j in range (selected[1], selected2[1]+1):
                                casilla = casilla + 1
                                selectedM[casilla] = [i,j]
                        # print (selectedM) 
                
                    
                if event.type == pygame.MOUSEWHEEL:   
                    # print (event.y)
                    zooms.zoom(event.y)
                    

                #if event.type == pygame.KEYDOWN:
                    # print(event.key)
            if menu_abierto or clicking[1]:
                menu_abierto = menu_prueba.draw_menu((0,0), pantallita, pygame.mouse.get_pos(), clicking[1])
            clock.tick(60)
            pygame.display.update()        

class mouse:

    def __init__(self, xy, num):
        self.xy = xy
        self.num = num

    def posMouse(self):
        return [self.xy[0] - movex, self.xy[1] - movey]

    def click(self):
        if self.num == 1:
            h = selecCasilla.selecCasilla(self.xy)
            print(h)
            return (h)
        else:
            return [-1,-1]

    def selecMulti(self):
        pass
        

class border:

    def check(m, eje):
        global movex, movey
        if eje[0] < map_size[0]:
            if m[0] >= screen_size[0]-20:
                movex -= int(vel_mov_mapa[0] * zoomv/3)
        if eje[0] > 0 :
            if m[0] <= 20:
                movex += int(vel_mov_mapa[0] * zoomv/3)
        if eje[1] < map_size[1]:
            if m[1] >= screen_size[1]-20:
                movey -= int(vel_mov_mapa[1] * zoomv/3)
        if eje[1] > 0 :        
            if m[1] <= 20:
                movey += int(vel_mov_mapa[1] * zoomv/3)


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
        for i in range (map_sizex[0], map_size[0]):
            for j in range (map_sizey[0], map_size[1]):
                if y < (j+1) * zoomv and y > (j) * zoomv :
                    var = j
                    break
            if x < (i+1) * zoomv and x > (i) * zoomv:
                var2 = i
                break
        if var == -1 or var2 == -1:
            return [-1,-1]
        return [var2,var]

class selecUnits:

    def selecUnits(madDic):
        var = 0
        unitsSelected = {}
        for i in len(selectedM):
            if madDic[selectedM[i]] == 1:
            
                unitsSelected[var] = selectedM[i]
                var = var + 1
        # print(unitsSelected)

class zooms:

    def zoom(evento):
        global zoomv, supmapa, movex, movey, map_size, mapaactual
        
        if evento > 0 and evento < 5:

            zoomv = zoomv * 2
            #limite de zoom maximo
            if zoomv > zoomvBase*8:
                zoomv = zoomvBase*8
            else:
                map_size =  [map_size[0] * 2, map_size[1] * 2]
                
                #movex = movex - (2 * ejeCoordenadas[0] - ejeCoordenadas[0])
                movex = movex - ejeCoordenadas[0]

                #movey = movey - (2 * ejeCoordenadas[1] - ejeCoordenadas[1])
                movey = movey - ejeCoordenadas[1]
                genMap.editMap

        if evento < 0 and evento > -5:
            
            zoomv = int(zoomv * 0.5)

            #limite de zoom minimo
            if zoomv < zoomvBase:
                zoomv = zoomvBase
            else:
                map_size =  [int(map_size[0] * 0.5), int(map_size[1] * 0.5)]
                movex = movex - int(0.5 * ejeCoordenadas[0] - ejeCoordenadas[0])
                movey = movey - int(0.5 * ejeCoordenadas[1] - ejeCoordenadas[1])
                genMap.editMap

        supmapa = pygame.Surface(map_size)
        #supmapa.fill(white)
        # print(zoomv)
        genMap.zoomMap()
        mapaactual = mapa(zoomv)
        mapaactual.create()


class genMap:
    
    def genMap():
        global mapDic, tilesInMap
        mapDic = {}
        tilesInMap = 0
        for i in range (map_sizex[0], map_size[0], zoomv):
            for j in range (map_sizey[0], map_size[1], zoomv):
                
                mapDic[tilesInMap] = {'img' : random.randint(0,1), 'pos' : (i,j)}
                mapDicXY[i,j] = {'img' : mapDic[tilesInMap], 'pos' : tilesInMap}
                tilesInMap = tilesInMap + 1

    def zoomMap():

        global mapDic
        var = 0
        for i in range (map_sizex[0], map_size[0], zoomv):
            for j in range (map_sizey[0], map_size[1], zoomv):
                
                mapDic[var]['pos'] = (i,j)
                var = var + 1
        #print(mapDic)
        
        #for i in range(tilesInMap):
        #    mapDic[var]['pos']      

    def editMap(i, j, var):
        global mapDic
        global mapTile
        mapDic[i]['img'] = var
        #mapTile[i,j]['img'] = var

class tile:

    def __init__(self, xy):
        self.xy = xy
        self.n = (1)
        self.img = mapDic[self.n]

    def tile(self):
        t = {'pos' : self.xy, 'visible' : True, 'visibleBy' : 1, 'img' : mapDic[self.n], 'unit' : False}
        return (t)
        #pass

'''class unit:

    def __init__(self):
        self.id
        self.name
        self.pos
        self.varDic = {}

    def unit():
        unitDic = {'id' : self.id, name : self.name, 'pos' : self.pos, 'varDic' : self.varDic}
        return u

class units:

    def unitsGen(self, numUnits):
        for i in range(numUnits):
            unitsDic[id]
    def editUnits(self, unit):
        global unitsDic
        untisDic[unit['id']] = unit'''

class tiles:
    def tiles():
        size = map_sizex[1] * map_sizey [1]
        for i in range (map_sizex[0], map_size[0], zoomv):
            for j in range (map_sizey[0], map_size[1], zoomv):
                t = tile([i,j])
                mapTile[i,j] = t.tile()


class mapa:
    def __init__(self, imgsize):
        self.imgsize = imgsize

    def create(self):
        
        for i in range (tilesInMap):
            #print(i)
            supmapa.blit(base_image[mapDic[i]['img']][zoomv],(mapDic[i]['pos']))



genMap.genMap()

tiles.tiles()

mapaactual = mapa(zoomv)


mapaactual.create()
game.play()