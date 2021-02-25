import pygame
#import Display
import logging
logger = logging.getLogger(__name__)

def draw_select_multi(clicked_map_origin, pantallita, movex, movey, map_size):
    # Dibuja cuadrado en pantalla
    # Necesita refactorizacion brutal XD
    mx, my =  pygame.mouse.get_pos()

    pixel_selected_x = min(max(min(clicked_map_origin[0], mx), movex), movex + map_size[0])
    pixel_selected_y = min(max(min(clicked_map_origin[1], my), movey), movey + map_size[1])
    pixel_other_pos_x = min(max(max(clicked_map_origin[0], movex), min(mx, movex + map_size[0])), movex + map_size[0]) 
    pixel_other_pos_y = min(max(max(clicked_map_origin[1], movey), min(my, movey + map_size[1])), movey + map_size[1])
    pygame.draw.rect(pantallita, (0,0,0), (pixel_selected_x, pixel_selected_y, abs(pixel_selected_x - pixel_other_pos_x), abs(pixel_selected_y - pixel_other_pos_y)), 5)

class Border:

    def check(m, eje, movex, movey, map_size, zoomv, screen_size, vel_mov_mapa):
        if eje[0] < map_size[0]:
            if m[0] >= screen_size[0]-20:
                movex -= int(vel_mov_mapa[0] * zoomv/1)
        if eje[0] > 0 :
            if m[0] <= 20:
                movex += int(vel_mov_mapa[0] * zoomv/1)
        if eje[1] < map_size[1]:
            if m[1] >= screen_size[1]-20:
                movey -= int(vel_mov_mapa[1] * zoomv/1)
        if eje[1] > 0 :        
            if m[1] <= 20:
                movey += int(vel_mov_mapa[1] * zoomv/1)
        
        return movex, movey

def _pos_mouse(xy, movex, movey):
    return [xy[0] - movex, xy[1] - movey]

class Mouse:

    def __init__(self, xy, num):
        self.xy = xy
        self.num = num

    def pos_mouse(self, movex, movey):
        return _pos_mouse(self.xy, movex, movey)

    def click(self, movex, movey, map_size, map_sizex, map_sizey, zoomv):
        if self.num == 1:
            h = SelecCasilla.selec_casilla(self.xy, movex, movey, map_size, map_sizex, map_sizey, zoomv)
            logger.info(f'Casilla clickada: {h}')
            return h
        else:
            return [-1, -1]

    def selec_multi(self):
        pass

class SelecCasilla:

    def selec_casilla(xy, movex, movey, map_size, map_sizex, map_sizey, zoomv):
        var = -1
        var2 = -1
        x, y = _pos_mouse(xy, movex, movey)
        for i in range (map_sizex[0], map_size[0]):
            for j in range (map_sizey[0], map_size[1]):
                if y < (j+1) * zoomv and y > (j) * zoomv :
                    var = j
                    break
            if x < (i+1) * zoomv and x > (i) * zoomv:
                var2 = i
                break
        if var2 == -1 or var == -1:
            return [-1, -1]
        return [var2,var]

class Zooms:

    def zoom(evento, zoomv, supmapa, movex, movey, map_size, zoom_base, eje_coordenadas, screen_filled_color, map_generator, images, screen_size, xy, mapaActual):
        
        if evento > 0 and evento < 5:
            zoomv = zoomv * 2
            #limite de zoom maximo
            if zoomv > zoom_base * 8:
                zoomv = zoom_base * 8
            else:
                map_size =  [map_size[0] * 2, map_size[1] * 2]
                
                #movex = movex - (2 * ejeCoordenadas[0] - ejeCoordenadas[0])
                movex = movex - xy[0]

                #movey = movey - (2 * ejeCoordenadas[1] - ejeCoordenadas[1])
                movey = movey - xy[1]
                

        if evento < 0 and evento > -5:
            
            zoomv = int(zoomv * 0.5)

            #limite de zoom minimo
            if zoomv < zoom_base:
                zoomv = zoom_base
            else:
                map_size =  [int(map_size[0] * 0.5), int(map_size[1] * 0.5)]
                movex = movex - int(0.5 * eje_coordenadas[0] - eje_coordenadas[0])
                movey = movey - int(0.5 * eje_coordenadas[1] - eje_coordenadas[1])
               
        supmapa.fill(screen_filled_color)
        supmapa = pygame.Surface(map_size, pygame.HWSURFACE)
        supmapa.fill(screen_filled_color)
        logger.info(zoomv)
        map_generator.zoom_map(map_size, zoomv)
        mapaActual.create(map_generator.map_list, images, supmapa, movex, movey, zoomv, screen_size)

        return supmapa, movex, movey, zoomv, map_size

    def minimap(evento, zoomv, supmapa, movex, movey, map_size, mapaactual, zoom_base, eje_coordenadas, screen_filled_color, map_generator, images, screen_size):
        '''    
        #if evento > 0 and evento < 5:
            zoomv = zoom_base
            
            map_size =  [map_size[0] * 2, map_size[1] * 2]
            
            #movex = movex - (2 * ejeCoordenadas[0] - ejeCoordenadas[0])
            movex = movex - eje_coordenadas[0]
            #movey = movey - (2 * ejeCoordenadas[1] - ejeCoordenadas[1])
            movey = movey - eje_coordenadas[1]
        '''        

        #if evento < 0 and evento > -5:
            
        

        
        map_size =  [int(map_size[0] * 2/zoom_base * (zoom_base/zoomv)), int(map_size[1] * 2/zoom_base * (zoom_base/zoomv))]

        zoomv = 2

    
        movex = map_size[0]//2 
        movey = map_size[1]//2
               

        supmapa = pygame.Surface(map_size)
        supmapa.fill(screen_filled_color)
        logger.info(zoomv)
        map_generator.zoom_map(map_size, zoomv)
        mapaactual.create(map_generator.map_list, images, supmapa, movex, movey, zoomv, screen_size)

        return supmapa, movex, movey, zoomv, map_size