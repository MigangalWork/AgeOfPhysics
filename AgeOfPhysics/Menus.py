import pygame

class Menus:
    def __init__(self, menu_width, menu_height, n_buttons, func_list, text_list):
        self.menu_width = menu_width
        self.menu_height = menu_height
        self.button_width = int(menu_width/n_buttons)
        self.button_height = int(menu_height/n_buttons)
        self.n_buttons = n_buttons
        self.func_list = func_list
        self.text = text_list

    def draw_menu(self, pos_xy, screen, mouse_xy, click):
        pos_x = pos_xy[0]
        for i in range(self.n_buttons):
            pos_y = pos_xy[1] + self.button_height*i
            button = pygame.Rect((pos_x, pos_y, self.button_width, self.button_height))
            pygame.draw.rect(screen, (100, 200, 0), button)
            pygame.draw.rect(screen, (0, 0, 0), button, 2)
            font = pygame.font.SysFont(None, 20)
            draw_text_centered(self.text[i], font, (0,0,0), screen, pos_x + self.button_width/2, pos_y + self.button_height/2)
            if button.collidepoint(mouse_xy) and click:
                eval(self.func_list[i])
                return False
        return True

def prueba_click(text):
    print(text)

def draw_text_centered(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    x -= textobj.get_width()/2
    y -= textobj.get_height()/2
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)