import pygame

def draw_text_centered(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    x -= textobj.get_width()/2
    y -= textobj.get_height()/2
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

class Menus:

    def __init__(self):
        self.menus_activos = {}

    def menu_clicked(self, xy):
        for menu_activo in self.menus_activos.values():
            if menu_activo.collidepoint(xy):
                return True
        return False

    def menu_add(self, x, y, width, height, id):
        menu = pygame.Rect((x, y, width, height))
        self.menus_activos[id] = menu
    
    def menu_erase(self, id):
        del self.menus_activos[id]

    def menu_draw(self, menus):
        for key in self.menus_activos.keys():
            x = menus[key]['x']
            y = menus[key]['y']
            width = menus[key]['width']
            height = menus[key]['height']
            screen = menus[key]['screen']
            pygame.draw.rect(screen, (0, 0, 0), (x,y,width, height))

class Menu:

    def __init__(self, x, y, width, height, screen, buttons, id, menus):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen = screen
        self.buttons = buttons
        self.id = id
        menus[id] = {'x' : self.x, 'y' : self.y, 'width' : self.width, 'height' : self.height, 'screen' : self.screen, 'buttons' : self.buttons}
        #self.surface = pygame.Surface((x,y))


    def activate_menu(self, my_menus): 
        my_menus.menu_add(self.x, self.y, self.width, self.height, self.id) 
        for i in self.buttons:
            key = self.buttons[i]
            x = buttons[key]['x']
            y = buttons[key]['y']
            width = buttons[key]['width']
            height = buttons[key]['height']
            Buttons.button_add(x, y, width, height, key)


class Buttons:

    def __init__(self):
        self.buttons_activos = {}

    def button_clicked(self, xy):
        for key, button_activo in self.buttons_activos.items():
            if button_activo.collidepoint(xy):         
                return key
        return -1

    def button_add(self, x, y, width, height, id):
        button = pygame.Rect((x, y, width, height))
        self.buttons_activos[id] = button
    
    def button_erase(id):
        del self.buttons_activos[id]

    def button_draw():
        for key in self.buttons_activos.keys():
            x = button[key]['x']
            y = button[key]['y']
            width = button[key]['width']
            height = button[key]['height']
            screen = button[key]['screen']
            pygame.draw.rect(screen, (255, 0, 0), (x,y,width, height))

class Button:

    def __init__(self, x, y, width, height, screen, function, id, buttons={}):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen = screen
        self.function
        self.id = id
        buttons[id] = {'x' : self.x, 'y' : self.y, 'width' : self.width, 'height' : self.height, 'screen' : self.screen, 'function' : self.function}


    def activate_button(self): 
        Buttons.button_add(self.x, self.y, self.width, self.height, self.id, self.function)
