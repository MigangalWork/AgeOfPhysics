import pygame

class Display:

    def __init__(self, movex, movey, zoomv, screen_size, images, screen_filled_color):
        self.movex = movex
        self.movey = movey
        self.zoomv = zoomv
        self.screen_size = screen_size
        self.images = images
        self.screen_filled_color = screen_filled_color


    def display(self, pantallita, supmapa, mapaactual, map_generator):

        pantallita.fill(self.screen_filled_color)
        pantallita.blit(supmapa, (0 + self.movex, 0 + self.movey))
        supmapa.fill(self.screen_filled_color)
        mapaactual.create(map_generator.map_list, self.images, supmapa, self.movex, self.movey, self.zoomv, self.screen_size)