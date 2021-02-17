from src.Menus import Menu
#from JuegoTest1 import pantallita

class MenuCreators:


    #Menu(x, y, width, height, screen, buttons, id):
    #Button(x, y, width, height, screen, buttons, id):

    def main_menus(screen, my_menus, menus):

        #topMenu = Menu(x, y, width, height, screen, buttons, id):
        
        #topMenuQuitB = Button(x, y, width, height, screen, buttons, id):
        pantallita = screen
        menu = Menu(0, 900, 1920, 180, pantallita, [], 00, menus)
        menu2 = Menu(0, 0, 1920, 80, pantallita, [], 10, menus)
    
        menu.activate_menu(my_menus)
        menu2.activate_menu(my_menus)
