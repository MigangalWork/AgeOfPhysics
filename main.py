import pygame, sys, random
import logging
logging.getLogger().setLevel(logging.INFO)

from src import config
from src.Map import GenMap, Mapa, Tiles, Chunks
from src.Menus import Menus, Buttons
from src import utils
from src.Text import Text
from src.Mouse import  draw_select_multi, Border, Mouse, Zooms
from src.GameObjets.ButtonsAndMenus import MenuCreators, Menus, Buttons
from src.Display import Display
from src.Events.Keyboard import Keyboard
from src.Events.MouseInput import MouseInput

import yaml

# Iniciamos el juego
pygame.init()
clock = pygame.time.Clock()

constructors = {}

variables = yaml.safe_load(open('variables.yaml', 'r'))
variables['clock'] = clock
constructors['clock'] = clock


class MainMenu:

    def mainMenu(variables):
        
         # Cargamos las variables
        screen_size = variables.get('screen_size')
        screen_filled_color = variables.get('colors').get('screen_filled')
        images = variables.get('images')
        map_sizex = variables.get('map_sizex')
        map_sizey = variables.get('map_sizey')
        images_dir = variables.get('images_dir')
        eje_coordenadas = variables.get('eje_coordenadas')
        vel_mov_mapa = variables.get('vel_mov_mapa')

        map_size = (map_sizex[1], map_sizey[1])
        variables['map_size'] = map_size
        
        #Cargamos las imagenes de los menus
        images = {}

        # Creamos la pantalla    
        display = Display(screen_size, images, screen_filled_color)
        variables['display'] = display
        constructors['display'] = display
        pantallita = display.pantallita

        #Creamos menus
        menu_creator = MenuCreators(screen_size)
        variables['menu_creator'] = menu_creator
        constructors['menu_creator'] = menu_creator
        menu_creator.create_menus(pantallita)
        menu_creator.main_screen_menus()

        text = Text(pantallita, {'x' : 200, 'y' : 200, 'width' : 200, 'height' : 40}, 20, (255,255,255))

        run = True
        text_active = False

        while run:


            #Pintamos la pantalla
            #display.display(mapaActual, map_generator, movex, movey, zoomv, supmapa)
           
            if text_active == True:
                text.textUpdate()

            #Pintamos menus
            
            menu_creator.Menus.menu_draw()
            menu_creator.Buttons.button_draw()
            
            #Miramos que eventos ocurren

            for event in pygame.event.get():

                #Miramos si se pulsa la X, de ser asi cerramos el juego
                if event.type == pygame.QUIT:
                    sys.exit()
                    run = False

                #Miramos si se pulsa la un boton del raton

                if event.type == pygame.MOUSEBUTTONDOWN:
                    
                    MouseInput.clickInput(event, variables, constructors)
                    '''
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
                    '''
                '''
                if event.type == pygame.MOUSEBUTTONUP:

                    clicking[event.button] = False
    
                if text_active == True:
                    text.textEdit(event)
                    text.textUpdate()
                '''
            clock.tick(60)
            pygame.display.update()  
        
        pygame.quit()
        return True


# Corremos el juego
MainMenu.mainMenu(variables)
result = Game.play(variables)
sys.exit()