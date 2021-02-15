import pygame
from VariablesGlobales import menusActivos, menus, buttons, buttonsActivos
#from JuegoTest1 import *
'''
class Menus:
    def __init__(self, menu_width, menu_height, n_buttons, func_list, text_list):
        self.menu_width = menu_width
        self.menu_height = menu_height
        self.button_width = int(menu_width/n_buttons)
        self.button_height = int(menu_height/n_buttons)
        self.n_buttons = n_buttons
        self.func_list = func_list
        self.text = text_list

    def draw_menu(self, pos_xy, screen, mouse_xy, click):
        pos_x = pos_xy[0]
        for i in range(self.n_buttons):
            pos_y = pos_xy[1] + self.button_height*i
            button = pygame.Rect((pos_x, pos_y, self.button_width, self.button_height))
            pygame.draw.rect(screen, (100, 200, 0), button)
            pygame.draw.rect(screen, (0, 0, 0), button, 2)
            font = pygame.font.SysFont(None, 20)
            draw_text_centered(self.text[i], font, (0,0,0), screen, pos_x + self.button_width/2, pos_y + self.button_height/2)
            if button.collidepoint(mouse_xy) and click:
                eval(self.func_list[i])
                return False
        return True
def prueba_click(text):
    print(text)
'''
def draw_text_centered(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    x -= textobj.get_width()/2
    y -= textobj.get_height()/2
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)




class Menus:

    def menuClicked(xy):
        for menuActivo in menusActivos.values():
            if menuActivo.collidepoint(xy):
                print(menu)
                return True
        return False

    def test(x):
        return x.collidepoint(xy)

    def menuClicked_alternative(xy):
        return any(map(lambda x: x.collidepoint(xy), menusActivos.values()))

    def menuAdd(x,y,width,height,id):
        global menusActivos
        menu = pygame.Rect((x, y, width, height))
        menusActivos[id] = menu
        print(menusActivos)
    
    def menuErase(id):
        del menusActivos[id]

    def menuDraw():
        for key in menusActivos.keys():
            #myIter = iter(menusActivos) no se como usarlo pero es significativamente mas eficiente y nos vendira bien
            #key = next(myIter)
            x = menus[key]['x']
            y = menus[key]['y']
            width = menus[key]['width']
            height = menus[key]['height']
            screen = menus[key]['screen']
            #pantallita.blit(key, (0,0))

            pygame.draw.rect(screen, (0, 0, 0), (x,y,width, height))

class Menu:

    def __init__(self, x, y, width, height, screen, buttons, id):
        global menus
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen = screen
        self.buttons = buttons
        self.id = id
        menus[id] = {'x' : self.x, 'y' : self.y, 'width' : self.width, 'height' : self.height, 'screen' : self.screen, 'buttons' : self.buttons}
        #self.surface = pygame.Surface((x,y))


    def activateMenu(self): 
        Menus.menuAdd(self.x, self.y, self.width, self.height, self.id) 
        for i in self.buttons:
            key = self.buttons[i]
            x = button[key]['x']
            y = button[key]['y']
            width = button[key]['width']
            height = button[key]['height']
            Buttons.buttonAdd(x,y,width,height,key)


class Buttons:

    def buttonClicked(xy):
        for i in range(0,len(buttonsActivos)):
            key = list(buttonsActivos.keys())[i]
            if buttonsActivos[key].collidepoint(xy):
                
                return key
        return -1

    def buttonAdd(x,y,width,height,id):
        global buttonsActivos
        button = pygame.Rect((x, y, width, height))
        buttonsActivos[id] = button
    
    def buttonErase(id):
        del buttonsActivos[id]

    def buttonDraw():
        for i in range(0,len(buttonsActivos)):
            #myIter = iter(menusActivos) no se como usarlo pero es significativamente mas eficiente y nos vendira bien
            #key = next(myIter)
            key = list(menusActivos.keys())[i]
            x = button[key]['x']
            y = button[key]['y']
            width = button[key]['width']
            height = button[key]['height']
            screen = button[key]['screen']
            pygame.draw.rect(screen, (255, 0, 0), (x,y,width, height))

class Button:

    def __init__(self, x, y, width, height, screen, function, id):
        global menus
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen = screen
        self.function
        self.id = id
        buttons[id] = {'x' : self.x, 'y' : self.y, 'width' : self.width, 'height' : self.height, 'screen' : self.screen, 'function' : self.function}


    def activateButton(self): 
        Buttons.buttonAdd(self.x, self.y, self.width, self.height, self.id, self.function)
