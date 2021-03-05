import pygame

class Menus:

    def __init__(self):
        self.menus_activos = {}
        self.menus = {}

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

    def menu_draw(self):
        for key in self.menus_activos.keys():
            x = self.menus[key].x
            y = self.menus[key].y
            width = self.menus[key].width
            height = self.menus[key].height
            screen = self.menus[key].screen
            
            screen.blit(self.menus[key].menu_surf,(x,y))
            pygame.draw.rect(self.menus[key].menu_surf, (0, 100, 0), (x,y,width, height))

    def menu_create(self, x, y, width, height, screen, buttons, id):

        menu = Menu(x, y, width, height, screen, buttons, id, self.menus)       

class Menu:

    def __init__(self, x, y, width, height, screen, buttons, id, menus, dynamicButtons = {}):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen = screen
        self.buttons = buttons
        self.menu_surf = pygame.Surface((self.width, self.height))
        self.id = id
    
        menus[id] = self


    def activate_menu(self, Menus, Buttons): 
        Menus.menu_add(self.x, self.y, self.width, self.height, self.id) 
        for i in self.buttons:
            key = i
            if key == 'dynamic':
                Buttons.button_create(self.dynamicButtons[key][x], y, width, height, screen, function, id)
            
            Buttons.button_add(key)


class Buttons:

    def __init__(self):
        self.buttons_activos = {}
        self.buttons = {}

        #Creamos un tipo de texto para textos generales de botones
        FONTNAMES = ["notosanscjktcregular", "notosansmonocjktcregular" ,
            "notosansregular,", 
            "microsoftjhengheimicrosoftjhengheiuilight",
            "microsoftyaheimicrosoftyaheiuilight",
            "msgothicmsuigothicmspgothic",
            "msmincho",
            "Arial"]

        self.FONTNAMES = ",".join(str(x) for x in FONTNAMES)
        self.Font = pygame.font.SysFont(FONTNAMES, 20)


    def button_clicked(self, xy):
        for key, button_activo in self.buttons_activos.items():
            if button_activo.collidepoint(xy):         
                return key
        return '-1'

    def button_add(self, key):
        x = self.buttons[key].x
        y = self.buttons[key].y
        width = self.buttons[key].width
        height = self.buttons[key].height
        button = pygame.Rect((x, y, width, height))
        self.buttons_activos[key] = button
    
    def button_erase(self,id):
        del self.buttons_activos[id]

    def button_draw(self):
        for key in self.buttons_activos.keys():
            x = self.buttons[key].x
            y = self.buttons[key].y
            width = self.buttons[key].width
            height = self.buttons[key].height
            screen = self.buttons[key].screen
            screen.blit(self.buttons[key].button_surf,(x,y))
            pygame.draw.rect(self.buttons[key].button_surf, (255, 0, 0), (0,0,width, height))
            
            self.draw_text_centered()
    
    def draw_text_centered(self, font = None, color = (0,0,255)):

        if font == None:
            font = self.Font
            

        for key in self.buttons_activos.keys():

            background = self.buttons[key].color

            x = self.buttons[key].width // 2
            y = self.buttons[key].height // 2

            textSurf = pygame.font.Font.render(font, self.buttons[key].text, 1, color)

            #textSurf = textObj[0]
            x -= pygame.Surface.get_width(textSurf)//2
            y -= pygame.Surface.get_height(textSurf)//2

            #textRect = textObj[1]
            #textRect.topleft = (x, y)

            self.buttons[key].button_surf.blit(textSurf, (x,y))


    def button_create(self, x, y, width, height, screen, function, id, text = 'texto', color = None):

        button = Button(x, y, width, height, screen, function, id, self.buttons, text, color)   

class Button:

    def __init__(self, x, y, width, height, screen, function, id, buttons, text = 'texto', color = None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen = screen
        self.function = function
        self.id = id
        self.button_surf = pygame.Surface((self.width, self.height))
        self.text = text
        self.color = color
        buttons[id] = self


    def activate_button(self, Buttons): 
        Buttons.button_add(self.x, self.y, self.width, self.height, self.id)
