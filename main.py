import pygame, sys, random
import logging
logging.getLogger().setLevel(logging.INFO)

from src import config
from src.Map import GenMap, Mapa, Tiles, Chunks
from src.Menus import Menus, Buttons
from src import utils
from src.Text import Text
from src.Mouse import  draw_select_multi, Border, Mouse, Zooms
from src.ButtonsAndMenus import MenuCreators, Menus, menusObj
from src.Display import Display

import yaml

# Iniciamos el juego
pygame.init()
clock = pygame.time.Clock()

variables = yaml.safe_load(open('variables.yaml', 'r'))

class Game:

    def play(variables):

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
        menus = variables.get('menus')
        eje_coordenadas = variables.get('eje_coordenadas')
        vel_mov_mapa = variables.get('vel_mov_mapa')
        zoom_base = variables.get('zoom_base')

        map_size = (map_sizex[1], map_sizey[1])
        zoom_list = list(map(lambda x: zoomv * x, zoom_list_refs))
        zoom_list.append(2)

        minimapa = False

        # Creamos la pantalla
        pantallita = pygame.display.set_mode(screen_size)
        supmapa = pygame.Surface(map_size)
        pantallita.blit(supmapa, (0,0))

        # Creamos el mapa
        map_generator = GenMap()
        images = utils.charge_images(images, zoom_list, images_dir)
        chunk = Chunks(images)
        map_generator.chunk(map_size, map_sizex, map_sizey, zoomv, chunk)
        map_generator.gen_map(map_size, images, chunk)
        map_tile = Tiles.tiles(map_size, map_sizex, map_sizey, zoomv, map_generator.map_list)
        mapaactual = Mapa(zoomv)
        mapaactual.create(map_generator.map_list, images, supmapa, movex, movey, zoomv, screen_size)
        
        #Creamos menus
        menu_creator = MenuCreators(menus,screen_size)
        menu_creator.create_menus(pantallita, menusObj)
        menu_creator.main_menus(menusObj)

        text = Text(pantallita, {'x' : 200, 'y' : 200, 'width' : 200, 'height' : 40}, 20, (255,255,255))

        run = True
        text_active = False
        click_map = False
        clicking = {1 : False}
        selected = []
        clicked_map_origin = [0, 0]
        display = Display(movex, movey, zoomv, screen_size, images, screen_filled_color)

        
        
        while run:


            #Pintamos la pantalla
            
            #display.display(pantallita, supmapa, mapaactual, map_generator)

            pantallita.fill(screen_filled_color)
            pantallita.blit(supmapa, (0 + movex, 0 + movey))
            supmapa.fill(screen_filled_color)
            mapaactual.create(map_generator.map_list, images, supmapa, movex, movey, zoomv, screen_size)

            if text_active == True:
                text.textUpdate()

            #Pintamos unidades

            #Pintamos menus
            Menus.menu_draw(menus)

            #Actualizacion de variables
            eje_coordenadas = [int(screen_size[0]/2) - movex, int(screen_size[1]/2) - movey]
            
            if click_map and clicking[1]:
                draw_select_multi(clicked_map_origin, pantallita, movex, movey, map_size)

            #Vemos si el raton esta en algun borde para mover el mapa
            movex, movey = Border.check(pygame.mouse.get_pos(), eje_coordenadas, movex, movey, map_size, zoomv, screen_size, vel_mov_mapa)
            
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
                        supmapa, movex, movey, zoomv, map_size = Zooms.minimap(event, zoomv, supmapa, movex, movey, map_size, mapaactual, zoom_base, eje_coordenadas, screen_filled_color, map_generator, images, screen_size)
                    elif pressed[pygame.K_m]:
                        supmapa = oldVar[0]
                        movex = oldVar[1]
                        movey = oldVar[2]
                        zoomv = oldVar[3]
                        map_size = oldVar[4]
                        supmapa, movex, movey, zoomv, map_size = Zooms.zoom(-1, zoomv, supmapa, movex, movey, map_size, mapaactual, zoom_base, eje_coordenadas, screen_filled_color, map_generator, images, screen_size)
                        minimapa = False

                if event.type == pygame.MOUSEBUTTONDOWN:

                    clicking[event.button] = True

                    #definimos el objeto click
                    click = Mouse(pygame.mouse.get_pos(), event.button)

                    #Variables de click
                    button = event.button
                    clicked = pygame.mouse.get_pos()

                    clicked_map = click.pos_mouse(movex, movey)
                    clicked_map_origin = pygame.mouse.get_pos()
                    if Menus.menu_clicked(clicked) == True:
                        # Crear objeto de Buttons antes de usarlo
                        # key = Buttons.button_clicked(clicked)
                        text_active = True
                    else:
                        text_active = False
                        selected = click.click(movex, movey, map_size, map_sizex, map_sizey, zoomv)
                        click_map = True

                if event.type == pygame.MOUSEBUTTONUP:

                    clicking[event.button] = False
                    click_map = False
                    if click_map:
                        pass
                    else:
                        pass
                    unclicked = pygame.mouse.get_pos()
                    
                    selected2 = click.click(movex, movey, map_size, map_sizex, map_sizey, zoomv)   

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
                    if minimapa == True:
                        pass
                    else:
                        supmapa, movex, movey, zoomv, map_size = Zooms.zoom(event.y, zoomv, supmapa, movex, movey, map_size, mapaactual, zoom_base, eje_coordenadas, screen_filled_color, map_generator, images, screen_size)

                if text_active == True:
                    text.textEdit(event)
                    text.textUpdate()

            clock.tick(60)
            pygame.display.update()  
        
        pygame.quit()
        return True
        


# Corremos el juego
result = Game.play(variables)
sys.exit()