import pygame
import yaml
import random

# Cargamos las variables, traer como parametros?
variables = yaml.safe_load(open('variables.yaml', 'r'))
map_sizex = variables.get('map_sizex')
map_sizey = variables.get('map_sizey')
zoomv = variables.get('zoomv')

class GenMap:

    def __init__(self):
        self.map_list = None
        self.map_list_XY = None
    
    def gen_map(self, map_size, images):
        # Esta funcion genera el mapa en base al tamaño y zoom
        self.map_list = []
        self.map_list_XY = []
        tiles_in_map = 0

        for i in range (map_sizex[0], map_size[0], zoomv):
            for j in range (map_sizey[0], map_size[1], zoomv): 
                lista = self._select_img(images)
                tile_dic = {'img' : lista[2], 'imgCat' : lista[0], 'imgGrp' : lista[1], 'pos' : (i,j)}
                self.map_list.append(tile_dic)
                self.map_list_XY.append({'img' : tile_dic, 'pos' : tiles_in_map}) 
                tiles_in_map += 1

    def zoom_map(self, map_size, zoomv):
        # Esta función cambia el tamaño del mapa
        var = 0
        for i in range (map_sizex[0], map_size[0], zoomv):
            for j in range (map_sizey[0], map_size[1], zoomv):   
                self.map_list[var]['pos'] = (i,j)
                var +=  1   

    def edit_map(self, i, j, var):
        # Esta funcion edita un elemento del mapa
        self.map_list[i]['img'] = var

    def _select_img(self, images):
        
        var = random.randint(0,len(images.keys())-1)
        cat = list(images.keys())[var]

        var = random.randint(0,len(images[cat].keys())-1)
        grp = list(images[cat].keys())[var]

        var = random.randint(0, len(images[cat][grp])-1)
        img = var

        lista = (cat,grp,img)
        return lista

    def chunk():
        chunkList = ('desert','winter','normal','sea','mountains')
        chunkMap = {}
        var = 0
        for i in range (map_sizex[0], map_size[0], zoomv*10):
            for j in range (map_sizey[0], map_size[1], zoomv*10):
                chunkMap[var] = chunkList[random.randint(0,len(chunkList))]


class Mapa:
    def __init__(self, imgsize):
        self.imgsize = imgsize

    def create(self, map_list, images, supmapa, movex, movey, zoomv, screen_size):
        # Esta función dibuja el mapa
        cero_pantalla = (-movex , -movey)
        for tile in map_list:
            #Imprimimos solo la parte de mapa dentro de la pantalla 
            if tile['pos'][0] > cero_pantalla[0] - 2 * zoomv and cero_pantalla[0] + screen_size[0] + zoomv > tile['pos'][0]:
                if tile['pos'][1] > cero_pantalla[1] - 2 * zoomv and cero_pantalla[1] + screen_size[1] + zoomv > tile['pos'][1]:
                    supmapa.blit(images[tile['imgCat']][tile['imgGrp']][tile['img']][zoomv], (tile['pos']))
class Tile:

    def __init__(self, xy, map_list):
        self.xy = xy
        self.n = (1)
        self.img = map_list[self.n]

    def tile(self):
        return {'pos' : self.xy, 'visible' : True, 'visibleBy' : 1, 'img' : self.img, 'unit' : False}

class Tiles:

    def tiles(map_size, map_sizex, map_sizey, zoomv, map_list, map_tile={}):
        size = map_sizex[1] * map_sizey[1]
        for i in range (map_sizex[0], map_size[0], zoomv):
            for j in range (map_sizey[0], map_size[0], zoomv):
                t = Tile([i,j], map_list)
                map_tile[i,j] = t.tile()
        return map_tile