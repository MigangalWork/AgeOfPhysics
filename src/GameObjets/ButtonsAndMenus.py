from src.Menus import Menus, Buttons
from src.Text import Text


class MenuCreators:

    #Menu(x, y, width, height, screen, buttons, id):
    #Button(x, y, width, height, screen, functions, id):

    def __init__(self, screen_size):

        self.Menus = Menus()
        self.Buttons = Buttons()
        self.Text = Text()

        self.screen_size = screen_size

    def create_menus(self, screen):  

        pantallita = screen
        listaBotones = []
        
        #Creamos los menus y sus botones

        #Pantalla de inicio
        listaBotones.append('I0000', 'I0010')
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
        button_1_menu_1 = self.Buttons.button_create(int(self.screen_size[0] * 0.3), int(self.screen_size[1] * 0.5), int(self.screen_size[0] * 0.4), int(self.screen_size[1] * 0.1), self.Menus.menus['I00'].menu_surf, [], 'I0010', '')
        
        x = pygame.Surface.get_width(self.Buttons.buttons['I0010'].button_surf) * 3 //2
        y = pygame.Surface.get_height(self.Buttons.buttons['I0010'].button_surf) - 5
        
        text = Text.text_create(self.Buttons.buttons['I0010'].button_surf, {'x' : x, 'y' : y, 'width' : 200, 'height' : 40}, 10, (255,255,255), 'TI0010')

        #Menus principales del juego

        button_1_menu_1 = self.Buttons.button_create(self.Menus.menus['00'].width//100, self.Menus.menus['00'].height//20, self.Menus.menus['00'].width//10, self.Menus.menus['00'].height//10, self.Menus.menus['00'].menu_surf, [], '0000')

        #Bottones dinamicos

    def dynamic_button(self, dynamicButtonAttrib):

        id = 'dynamic.' + dynamicButtonAttrib.get('num', '0')
        x = dynamicButtonAttrib[x]
        y = 
        width =
        height =
        screen = 
        function =
        button_dinamico = self.Buttons.button_create(x, y, width, height, screen, function, id, text = 'texto', color = None)

    def delete_menus(self, id):
        self.Menus.menu_erase(id)

    def main_screen_menus(self):
        self.Menus.menus['I00'].activate_menu(self.Menus, self.Buttons)
        self.Text.text_add('TI0010')


    def main_menus(self):

        #topMenu = Menu(x, y, width, height, screen, buttons, id):
        
        #topMenuQuitB = Button(x, y, width, height, screen, buttons, id):
        
        self.Menus.menus['00'].activate_menu(self.Menus, self.Buttons)
        self.Menus.menus['10'].activate_menu(self.Menus, self.Buttons)
