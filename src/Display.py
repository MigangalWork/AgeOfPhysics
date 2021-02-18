import pygame

class Display:

    def __init__(self, movex, movey, zoomv, screensize, pantallita, supmapa, mapaactual, map_generator, images, screen_filled_color):
        self.movex = movex
        self.movey = movey
        self.zoomv = zoomv
        self.screensize = screensize
        self.supmapa = supmapa 
        self.mapaactual = mapaactual
        self.map_generator = map_generator
        self.images = images
        self.screen_filled_color = screen_filled_color

    def display():

        pantallita.fill(screen_filled_color)
        pantallita.blit(supmapa, (0 + movex, 0 + movey))
        supmapa.fill(screen_filled_color)
        mapaactual.create(map_generator.map_list, images, supmapa, movex, movey, zoomv, screen_size)