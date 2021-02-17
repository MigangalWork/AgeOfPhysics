from src.Menus import Menu
#from JuegoTest1 import pantallita

class MenuCreators:


    #Menu(x, y, width, height, screen, buttons, id):
    #Button(x, y, width, height, screen, buttons, id):

    def main_menus(screen, my_menus, menus, screen_size):

        #topMenu = Menu(x, y, width, height, screen, buttons, id):
        
        #topMenuQuitB = Button(x, y, width, height, screen, buttons, id):
        pantallita = screen
        menu = Menu(0, int(screen_size[1] * 0.8), screen_size[0], int(screen_size[1] * 0.2), pantallita, [], 00, menus)
        menu2 = Menu(0, 0, screen_size[0], int(screen_size[1] * 0.1), pantallita, [], 10, menus)
    
        menu.activate_menu(my_menus)
        menu2.activate_menu(my_menus)
