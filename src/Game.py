import pygame, sys, random
import multiprocessing
import logging
logging.getLogger().setLevel(logging.INFO)

from src import config
from src.Map import GenMap, MapaString, Tiles, Chunks
from src.Menus import Menus, Buttons
from src import utils
from src.Text import Text
from src.Mouse import  draw_select_multi, Border, Mouse, Zooms
from src.GameObjets.ButtonsAndMenus import MenuCreators
from src.GameObjets.ArmiesAndUnits import UnitsCreators
from src.Display import Display
from src.Events.Keyboard import Keyboard
from src.Events.MouseInput import MouseInput

class Test:

    def __init__(self, a = 1):

        self.a = a
            
    def printear(self, b):

        print(self.a)
        print(b)

class Game:

    def play(variables, constructors, superficies):
        print('Iniciando Juego')
        # Cargamos las variables
        screen_size = variables.get('screen_size')
        screen_filled_color = variables.get('colors').get('screen_filled')
        movex = variables.get('movex')
        movey = variables.get('movey')
        zoomv = variables.get('zoomv')
        images = variables.get('images')
        zoom_list_refs = variables.get('zoom_list_refs')
        map_sizex = variables.get('map_sizex')
        map_sizey = variables.get('map_sizey')
        images_dir = variables.get('images_dir')
        eje_coordenadas = variables.get('eje_coordenadas')
        vel_mov_mapa = variables.get('vel_mov_mapa')
        zoom_base = variables.get('zoom_base')

        map_size = (map_sizex[1], map_sizey[1])
        variables['map_size'] = map_size
        zoom_list = list(map(lambda x: zoomv * x, zoom_list_refs))
        zoom_list.append(2)

        minimapa = False

        display = constructors['display']
        menu_creator = constructors['menu_creator']
        clock = constructors['clock']
        
        #Cargamos las imagenes en memoria
        images, imagesString = utils.charge_images(images, zoom_list, images_dir)
        variables['images'] = imagesString
        superficies['images'] = images

        # Creamos los mapas de la pantalla

        display.images = images
        #display.image()
        display.maps(map_size)
        pantallita = display.pantallita
        maps = display.returnMaps()
        variables['maps'] = maps
        variables['supmapa'] = maps[0]
        supmapa = maps[0]

        # Creamos el mapa
        map_generator = GenMap()
        constructors['map_generator'] = map_generator
        chunk = Chunks(images)
        constructors['chunk'] = chunk
        map_generator.chunk(map_size, map_sizex, map_sizey, zoomv, chunk)
        map_generator.gen_map(map_size, images, chunk)

        #map_tile = Tiles.tiles(map_size, map_sizex, map_sizey, zoomv, map_generator.map_list)
        mapaActual = MapaString(zoomv)
        constructors['mapaActual'] = mapaActual

        mapaActual.create(map_generator.map_list, images, movex, movey, zoomv, map_size)
        
        
        #Creamos menus
        '''
        menu_creator = MenuCreators(screen_size)
        menu_creator.create_menus(pantallita, menusObj, menu_creator)
        '''

        menu_creator.main_menus()
        
        text = Text(pantallita, {'x' : 200, 'y' : 200, 'width' : 200, 'height' : 40}, 20, (255,255,255))





        #Creamos Unidades
        unitsCreator = UnitsCreators(variables)
        variables['unitsCreator'] = unitsCreator


        run = True
        text_active = False
        click_map = False
        clicking = {1 : False}
        selected = []
        clicked_map_origin = [0, 0]
        
        test = Test()

        #screenProcess = multiprocessing.Process(target=test.printear, args=('10'))
        #screenProcess.start()
        
        #Creamos el mapa en si
        display.displayCreate(constructors['mapaActual'], constructors['map_generator'], variables['movex'], variables['movey'], variables['zoomv'], pygame.image.tostring(variables['supmapa'], 'RGB'), variables['map_size'])



        while run:


            #Pintamos la pantalla
            
            #screenProcess = multiprocessing.Process(target=display.display, args=(constructors['mapaActual'], constructors['map_generator'], variables['movex'], variables['movey'], variables['zoomv'], pygame.image.tostring(variables['supmapa'], 'RGB'), variables['map_size']))
            display.display(constructors['mapaActual'], constructors['map_generator'], variables['movex'], variables['movey'], variables['zoomv'], pygame.image.tostring(variables['supmapa'], 'RGB'), variables['map_size'])
            
            '''
            pantallita.fill(screen_filled_color)
            pantallita.blit(supmapa, (0 + movex, 0 + movey))
            supmapa.fill(screen_filled_color)
            mapaactual.create(map_generator.map_list, images, supmapa, movex, movey, zoomv, screen_size)
            '''
            if text_active == True:
                text.textUpdate()

            #Pintamos unidades

            #Pintamos menus
            menu_creator.Menus.menu_draw()
            menu_creator.Buttons.button_draw()

            #Actualizacion de variables
            variables['eje_coordenadas'] = [int(screen_size[0]/2) - variables['movex'], int(screen_size[1]/2) - variables['movey']]
            
            if click_map and clicking[1]:
                draw_select_multi(clicked_map_origin, pantallita, movex, movey, map_size)

            #Vemos si el raton esta en algun borde para mover el mapa
            variables['movex'], variables['movey'] = Border.check(pygame.mouse.get_pos(), variables['eje_coordenadas'], variables['movex'], variables['movey'], variables['map_size'], variables['zoomv'], variables['screen_size'], variables['vel_mov_mapa'])
            
            #Miramos que eventos ocurren
            for event in pygame.event.get():
                
                #Miramos si se pulsa la X, de ser asi cerramos el juego
                if event.type == pygame.QUIT:

                    run = False

                #Miramos si se pulsa la un boton del raton
                if event.type == pygame.KEYDOWN:
                    pressed = pygame.key.get_pressed()
                    if pressed[pygame.K_m] and minimapa == False:
                        minimapa = True
                        oldVar = (supmapa, movex, movey, zoomv, map_size)
                        supmapa, movex, movey, zoomv, map_size = Zooms.minimap(event, zoomv, supmapa, movex, movey, map_size, mapaActual, zoom_base, eje_coordenadas, screen_filled_color, map_generator, images, screen_size)
                    elif pressed[pygame.K_m]:
                        supmapa = oldVar[0]
                        movex = oldVar[1]
                        movey = oldVar[2]
                        zoomv = oldVar[3]
                        map_size = oldVar[4]
                        supmapa, movex, movey, zoomv, map_size = Zooms.zoom(-1, zoomv, supmapa, movex, movey, map_size, mapaActual, zoom_base, eje_coordenadas, screen_filled_color, map_generator, images, screen_size, clicked_map)
                        minimapa = False

                if event.type == pygame.MOUSEBUTTONDOWN:

                    MouseInput.clickInput(event, variables, constructors)

                if event.type == pygame.MOUSEBUTTONUP:

                    clicking[event.button] = False
                    click_map = False
                    if click_map:
                        pass
                    else:
                        pass
                    unclicked = pygame.mouse.get_pos()
                    
                    #selected2 = click.click(movex, movey, map_size, map_sizex, map_sizey, zoomv)   

                    '''
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
                    '''               
                    
                if event.type == pygame.MOUSEWHEEL: 

                    MouseInput.wheelInput(event, variables, constructors)

                if text_active == True:
                    texto = text.textEdit(event)
                    text.textUpdate()
                    if texto != None:
                        textoSaved = texto
                        print(textoSaved)

            clock.tick(30)
            pygame.display.flip() 
        
        pygame.quit()
        return True