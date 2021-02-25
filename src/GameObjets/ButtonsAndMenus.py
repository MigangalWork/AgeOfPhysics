from src.Menus import Menus, Buttons


class MenuCreators:

    #Menu(x, y, width, height, screen, buttons, id):
    #Button(x, y, width, height, screen, functions, id):

    def __init__(self, screen_size):

        self.Menus = Menus()
        self.Buttons = Buttons()

        self.screen_size = screen_size

    def create_menus(self, screen):  

        pantallita = screen
        listaBotones = []
        
        #Creamos los menus y sus botones

        #Pantalla de inicio
        listaBotones.append('I0000')
        menu = self.Menus.menu_create(0, 0, self.screen_size[0], self.screen_size[1], pantallita, listaBotones, 'I00')
        listaBotones = []


        #Menus principales del juego
        listaBotones.append('0000')
        menu = self.Menus.menu_create(0, int(self.screen_size[1] * 0.8), self.screen_size[0], int(self.screen_size[1] * 0.2), pantallita, listaBotones, '00')
        listaBotones = []
        

        menu = self.Menus.menu_create(0, 0, self.screen_size[0], int(self.screen_size[1] * 0.1), pantallita, [], '10')

        self.create_buttons()

    def create_buttons(self):


        #Pantalla de inicio

        button_1_menu_1 = self.Buttons.button_create(int(self.screen_size[0] * 0.3), int(self.screen_size[1] * 0.4), int(self.screen_size[0] * 0.4), int(self.screen_size[1] * 0.1), self.Menus.menus['I00'].menu_surf, [], 'I0000')

        #Menus principales del juego

        button_1_menu_1 = self.Buttons.button_create(10, 10, 100, 100, self.Menus.menus['00'].menu_surf, [], '0000')


    def delete_menus(self, id):
        self.Menus.menu_erase(id)

    def main_screen_menus(self):
        self.Menus.menus['I00'].activate_menu(self.Menus, self.Buttons)


    def main_menus(self):

        #topMenu = Menu(x, y, width, height, screen, buttons, id):
        
        #topMenuQuitB = Button(x, y, width, height, screen, buttons, id):
        
        self.Menus.menus['00'].activate_menu(self.Menus, self.Buttons)
        self.Menus.menus['10'].activate_menu(self.Menus, self.Buttons)
