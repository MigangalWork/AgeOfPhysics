from src.Menus import Menu, Menus, Buttons, Button
#from JuegoTest1 import pantallita

Menus = Menus()
Buttons = Buttons()
menusObj = {}
buttonsObj = {}

class MenuCreators:

    #Menu(x, y, width, height, screen, buttons, id):
    #Button(x, y, width, height, screen, functions, id):

    def __init__(self, screen_size):

        self.menus = {}
        self.buttons = {}
        self.screen_size = screen_size

    def create_menus(self, screen, menusObj, menu_creator):  

        pantallita = screen
        listaBotones = []
        
        #Creamos los menus y sus botones

        #Pantalla de inicio
        listaBotones.append('I0000')
        menu = Menu(0, 0, self.screen_size[0], self.screen_size[1], pantallita, listaBotones, 'I00', self.menus, Menus.menus_surface_dic)
        menusObj['I00'] = menu



        #Menus principales del juego
        menu = Menu(0, int(self.screen_size[1] * 0.8), self.screen_size[0], int(self.screen_size[1] * 0.2), pantallita, [0000], 00, self.menus, Menus.menus_surface_dic)
        menusObj[00] = menu
        

        menu = Menu(0, 0, self.screen_size[0], int(self.screen_size[1] * 0.1), pantallita, [], 10, self.menus, Menus.menus_surface_dic)
        
        menusObj[10] = menu

        menu_creator.create_buttons(buttonsObj, menusObj)

    def create_buttons(self, buttonsObj, menusObj):


        #Pantalla de inicio

        button_1_menu_1 = Button(int(self.screen_size[0] * 0.3), int(self.screen_size[1] * 0.4), int(self.screen_size[0] * 0.4), int(self.screen_size[1] * 0.1), menusObj['I00'].menu_surf, [], 'I0000', self.buttons)
        buttonsObj['I0000'] = button_1_menu_1

        #Menus principales del juego

        button_1_menu_1 = Button(10, 10, 100, 100, menusObj[00].menu_surf, [], 0000, self.buttons)
        buttonsObj[0000] = button_1_menu_1

    def delete_menus(self, id):
        Menus.menu_erase(id)

    def main_screen_menus(self, menusObj):
        menusObj['I00'].activate_menu(Menus, Buttons, self.buttons)
    def del_main_screen_menus(self):
        Menus.menu_erase('I00')

    def main_menus(self, menusObj):

        #topMenu = Menu(x, y, width, height, screen, buttons, id):
        
        #topMenuQuitB = Button(x, y, width, height, screen, buttons, id):
        
        menusObj[00].activate_menu(Menus, Buttons, self.buttons)
        menusObj[10].activate_menu(Menus, Buttons, self.buttons)
