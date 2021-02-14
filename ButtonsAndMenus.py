from Menus import Menu
#from JuegoTest1 import pantallita

class MenuCreators:


    #Menu(x, y, width, height, screen, buttons, id):
    #Button(x, y, width, height, screen, buttons, id):
    
    
    def mainMenus(screen):

        #topMenu = Menu(x, y, width, height, screen, buttons, id):
        
        #topMenuQuitB = Button(x, y, width, height, screen, buttons, id):
        pantallita = screen
        menu = Menu( 0, 800, 1000, 200, pantallita, [], 00)
        menu.activateMenu()
        menu2 = Menu( 0, 0, 1000, 80, pantallita, [], 10)
        menu2.activateMenu()
