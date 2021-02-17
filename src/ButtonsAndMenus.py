from src.Menus import Menu, Menus, Buttons, Button
#from JuegoTest1 import pantallita

Menus = Menus()
Buttons = Buttons()
menusObj = {}

class MenuCreators:

    #Menu(x, y, width, height, screen, buttons, id):
    #Button(x, y, width, height, screen, functions, id):

    def __init__(self, menus, screen_size):

        self.menus = menus
        self.screen_size = screen_size

    def create_menus(self, screen, menusObj):  

        pantallita = screen
        menu = Menu(0, int(self.screen_size[1] * 0.8), self.screen_size[0], int(self.screen_size[1] * 0.2), pantallita, [], 00, self.menus)
        menu2 = Menu(0, 0, self.screen_size[0], int(self.screen_size[1] * 0.1), pantallita, [], 10, self.menus)
        menusObj[00] = menu
        menusObj[10] = menu2

    def main_menus(self, menusObj):

        #topMenu = Menu(x, y, width, height, screen, buttons, id):
        
        #topMenuQuitB = Button(x, y, width, height, screen, buttons, id):
        
        menusObj[00].activate_menu(Menus)
        menusObj[10].activate_menu(Menus)
    
    def create_buttons(self, screen):
        button_1 = Button(x, y, width, height, screen, function, id)
