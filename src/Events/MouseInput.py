import pygame
from src.Mouse import *
from src.Menus import *
from src.ButtonsAndMenus import Menus, Buttons
from src.EventsAndFunction import EventsFinder

clicking = {}

class MouseInput:

    

    def mouseInput(event, display):

        clicking[event.button] = True

        #definimos el objeto click
        click = Mouse(pygame.mouse.get_pos(), event.button)

        #Variables de click
        button = event.button
        clicked = pygame.mouse.get_pos()

        #clicked_map = click.pos_mouse(movex, movey)
        clicked_map_origin = pygame.mouse.get_pos()

        #Miramos si clickamos en un menu

        if Menus.menu_clicked(clicked) == True:
            
            key = Buttons.button_clicked(clicked)
            EventsFinder.findFunction(key, display)
            
        