import pygame

def draw_text_centered(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    x -= textobj.get_width()/2
    y -= textobj.get_height()/2
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

class Buildings:

    def __init__(self):
        self.menus_activos = {}
        self.menus_surface_dic = {}

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
            screen.blit(self.menus_surface_dic[key],(x,y))
            

class Building:

    def __init__(self, screen, image, id, buildings):

        self.screen = screen
        self.image = image
        self.atributes = atributes
        self.id = id
        buildings[id] = {'image' : image, 'screen' : self.screen, 'atributes' : self.atributes}



    def activate_menu(self, Menus, Buttons, buttons): 
        Menus.menu_add(self.x, self.y, self.width, self.height, self.id) 
        


class BuildinsInGame:

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
    
    def button_erase(self,id):
        del self.buttons_activos[id]

    def button_draw(self, buttons):
        for key in self.buttons_activos.keys():
            x = buttons[key]['x']
            y = buttons[key]['y']
            width = buttons[key]['width']
            height = buttons[key]['height']
            screen = buttons[key]['screen']
            pygame.draw.rect(screen, (255, 0, 0), (x,y,width, height))

class Button:

    def __init__(self, x, y, width, height, screen, function, id, buttons):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen = screen
        self.function = function
        self.id = id
        buttons[id] = {'x' : self.x, 'y' : self.y, 'width' : self.width, 'height' : self.height, 'screen' : self.screen, 'function' : self.function}


    def activate_button(self, Buttons): 
        Buttons.button_add(self.x, self.y, self.width, self.height, self.id)