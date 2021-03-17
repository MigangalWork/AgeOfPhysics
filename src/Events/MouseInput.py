import pygame
from src.Mouse import *
from src.Menus import *
from src.GameObjets.ArmiesAndUnits import Unit, Armies
from src.EventsAndFunction import EventsFinder

clicking = {}

class MouseInput:

    

    def clickInput(event, variables, constructors, superficies = None):

        menu_creator = constructors['menu_creator']

        unitsCreator = constructors.get('unitsCreator', None)

        variables['text_active'] = None
            
        
        
        clicking[event.button] = True
        variables['clicking'] = clicking

        #definimos el objeto click
        click = Mouse(pygame.mouse.get_pos(), event.button)
        constructors['click'] = click
        #Variables de click
        button = event.button
        clicked = pygame.mouse.get_pos()

        variables['clicked'] = clicked

        clicked_map = click.pos_mouse(variables['movex'], variables['movey'])

        #Miramos si clickamos en un menu

        if menu_creator.Menus.menu_clicked(clicked) == True:
            
            key = menu_creator.Buttons.button_clicked(clicked)
            print(key)
            EventsFinder.findFunction(key, variables, constructors, superficies)

        elif unitsCreator != None and unitsCreator.Armies.army_clicked(clicked) != '-1':
            
            key = unitsCreator.Armies.army_clicked(clicked)
            EventsFinder.findFunction(key, variables, constructors)

        
    def wheelInput(event, variables, constructors):

        menu_creator = constructors['menu_creator']

        click = Mouse(pygame.mouse.get_pos(), 5)

        #Variables de click

        clicked_map = click.pos_mouse(variables['movex'], variables['movey'])

        clicked = pygame.mouse.get_pos()
        variables['clicked'] = clicked


        if variables.get('minimapa', False) == True or menu_creator.Menus.menu_clicked(clicked) == True:
            pass

        else:
                        
            variables['supmapa'], variables['movex'], variables['movey'], variables['zoomv'], variables['map_size'] = Zooms.zoom(event.y, variables['zoomv'], variables['supmapa'], variables['movex'], variables['movey'], variables['map_size'], variables['zoom_base'], variables['eje_coordenadas'], variables['colors']['screen_filled'], constructors['map_generator'], variables['images'], variables['screen_size'], clicked_map, constructors['mapaActual'])
            
            


            
        