import pygame, sys, random, ctypes
import logging
logging.getLogger().setLevel(logging.INFO)

from src.config import startConfig
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

#Confiduraccion inicial

width, heigth = startConfig()

width = width//2
heigth = heigth//2

# Iniciamos el juego
pygame.init()
clock = pygame.time.Clock()

constructors = {}
superficies = {}

variables = yaml.safe_load(open('variables.yaml', 'r'))

constructors['clock'] = clock




class MainMenu:

    def mainMenu(variables, constructors, superficies):
        
         # Cargamos las variables
        #screen_size = variables.get('screen_size')
        screen_filled_color = variables.get('colors').get('screen_filled')
        images = variables.get('images')
        map_sizex = variables.get('map_sizex')
        map_sizey = variables.get('map_sizey')
        images_dir = variables.get('images_dir')
        eje_coordenadas = variables.get('eje_coordenadas')
        vel_mov_mapa = variables.get('vel_mov_mapa')

        map_size = (map_sizex[1], map_sizey[1])
        variables['map_size'] = map_size

        screen_size = (width, heigth)
        variables['screen_size'] = (width, heigth)
        
        #Cargamos las imagenes de los menus
        images = {}

        # Creamos la pantalla    
        display = Display(screen_size, images, screen_filled_color)
        display.screen()
        pantallita = display.pantallita
        
        constructors['display'] = display

        #Creamos menus
        menu_creator = MenuCreators(screen_size)
        constructors['menu_creator'] = menu_creator
        menu_creator.create_menus(pantallita)
        menu_creator.main_screen_menus()

        run = True
        variables['text_active'] = None

        while run:


            #Pintamos la pantalla
            #display.display(mapaActual, map_generator, movex, movey, zoomv, supmapa)
        

            #Pintamos menus
            
            menu_creator.Menus.menu_draw()
            menu_creator.Buttons.button_draw()
            menu_creator.Texts.text_draw()
            
            
            #Miramos que eventos ocurren

            for event in pygame.event.get():

                #Miramos si se pulsa la X, de ser asi cerramos el juego
                if event.type == pygame.QUIT:
                    sys.exit()
                    run = False

                #Miramos si se pulsa la un boton del raton

                if event.type == pygame.MOUSEBUTTONDOWN:
                    
                    MouseInput.clickInput(event, variables, constructors, superficies)
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

                if event.type == pygame.KEYDOWN:

                    pass

                if variables['text_active'] != None:
                        text = menu_creator.Texts.texts[variables['text_active']].textEdit(event)
                        #text.textUpdate()
                        if text != None:
                            textSaved = text
                            print(textSaved)


            clock.tick(30)
            pygame.display.update()  
        
        pygame.quit()
        return True


# Corremos el juego
MainMenu.mainMenu(variables, constructors, superficies)

sys.exit()