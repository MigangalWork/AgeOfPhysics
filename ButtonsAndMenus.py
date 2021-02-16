from Menus import Menu
#from JuegoTest1 import pantallita

class MenuCreators:


    #Menu(x, y, width, height, screen, buttons, id):
    #Button(x, y, width, height, screen, buttons, id):
    
    
    def mainMenus(screen):

        #topMenu = Menu(x, y, width, height, screen, buttons, id):
        
        #topMenuQuitB = Button(x, y, width, height, screen, buttons, id):
        pantallita = screen
        menu = Menu( 0, 900, 1920, 180, pantallita, [], 00)
        menu.activateMenu()
        menu2 = Menu( 0, 0, 1920, 80, pantallita, [], 10)
        menu2.activateMenu()
