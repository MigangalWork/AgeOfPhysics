import pygame
import yaml
import random

# Cargamos las variables, traer como parametros?
variables = yaml.safe_load(open('variables.yaml', 'r'))
map_sizex = variables.get('map_sizex')
map_sizey = variables.get('map_sizey')
zoomv = variables.get('zoomv')
tile_map = {}
map_dic_XY = {}
variables['map_dic_XY'] = map_dic_XY

class GenMap:

    def __init__(self):
        self.map_list = None
        self.map_dic_XY = None
    
    def gen_map(self, map_size, images, Chunk):
        # Esta funcion genera el mapa en base al tamaño y zoom
        

        self.map_list = []
        tiles_in_map = 0
        tile_dic = {}
        for i in range (map_sizex[0], map_size[0], zoomv):
            for j in range (map_sizey[0], map_size[1], zoomv): 
                #lista = self._select_img(images)

                self.map_list.append(self.map_dic_XY[i,j])

                lista = Chunk.chooseChunk(self.map_list, images, tiles_in_map, Chunk)

                tile_dic = {'imgCat' : lista[0], 'imgGrp' : lista[1], 'img' : lista[2], 'pos' : (i,j), 'chunk' : self.map_list[tiles_in_map]}

                self.map_list[tiles_in_map] = tile_dic
                self.map_dic_XY[i,j] = {'img' : tile_dic, 'pos' : tiles_in_map}
                Tile.tile(map_dic_XY,(i,j))
                tiles_in_map += 1

        GenMap.updateMapDic(self)


    def zoom_map(self, map_size, zoomv):
        # Esta función cambia el tamaño del mapa
        var = 0
        for i in range (map_sizex[0], map_size[0], zoomv):
            
            for j in range (map_sizey[0], map_size[1], zoomv):
              
                self.map_list[var]['pos'] = (i,j)
                var +=  1   

    def edit_map(self, i, j, var):
        # Esta funcion edita un elemento del mapa
        GenMap.updateSelfMapDic(self)

        pos = self.map_dic_XY[i,j]['pos']
        self.map_list[pos]['img'] = var[0]
        self.map_list[pos]['imgGrp'] = var[1]
        self.map_list[pos]['imgCat'] = var[2]

        GenMap.updateMapDic(self)

    def _select_img(self, images):
        
        var = random.randint(0,len(images.keys())-1)
        cat = list(images.keys())[var]

        var = random.randint(0,len(images[cat].keys())-1)
        grp = list(images[cat].keys())[var]

        var = random.randint(0, len(images[cat][grp])-1)
        img = var

        lista = (cat,grp,img)
        return lista

    def updateMapDic(self):

        map_dic_XY = self.map_dic_XY

    def updateSelfMapDic(self):

        self.map_dic_XY = map_dic_XY

    def chunk(self, map_size, map_sizex, map_sizey, zoomv, Chunk):
        self.map_dic_XY = {}
        chunk = 'sea'
        
        for x in range (map_sizex[0], map_size[0], zoomv):
            for y in range (map_sizey[0], map_size[1], zoomv):
                if (x,y) in self.map_dic_XY:
                    
                    pass
                else:
                    chunkOld = chunk
                    chunk = Chunk.addChunk(chunkOld)
                    self.map_dic_XY[x,y] = { 'chunk' : chunk }
                    ix = x + zoomv * random.randint(-1,1)
                    iy = y + zoomv * random.randint(-1,1)
                    mounVert = True
                    mounHor = True
                    while mounHor or mounVert:
                        if (ix,iy) in self.map_dic_XY:
                            
                            ix = ix + zoomv * random.randint(-1,1)
                            iy = iy + zoomv * random.randint(-1,1)
                            if ix > map_size[0] or iy > map_size[1]:
                                break
                            
                        else:
                            if random.random() > 0.0001 and mounHor:
                                self.map_dic_XY[ix,iy] = { 'chunk' : chunk }
                                ix = ix + zoomv * random.randint(-1,1)
                                if ix < 0:
                                    ix = 0
                                if ix > map_size[0]:
                                    ix = map_size[0]

                                
                                

                            else:
                                mounHor = False

                            if random.random() > 0.0001 and mounVert:
                                self.map_dic_XY[ix,iy] = { 'chunk' : chunk }
                                iy = iy + zoomv * random.randint(-1,1)
                                if iy < 0:
                                    iy = 0
                                if iy > map_size[1]:
                                    iy = map_size[1]
                                
                                
                            else:
                                mounVert = False
                                    
                            #self.map_dic_XY[x,y] = Chunk.randChunk(x, y, chunk, chunkOld, self.map_dic_XY)
                                
                    self.map_dic_XY = Chunk.mountains(x, y, self.map_dic_XY, chunk, map_size)
                #print(self.map_list)

        GenMap.updateMapDic(self)  

        '''
        for x in range (map_sizex[0], map_size[0], chunkSize):
            for y in range (map_sizey[0], map_size[1], chunkSize):
                chunkOld = chunk
                chunk = Chunk.addChunk(chunkOld)
                
                for x in range(i, i+chunkSize, zoomv):
                    for y in range(j, j+chunkSize, zoomv):
                        
                        self.map_dic_XY[x,y] = Chunk.randChunk(x, y, chunk, chunkOld, self.map_dic_XY)
                        
                        self.map_dic_XY = Chunk.mountains(x, y, self.map_dic_XY, chunk)
        #print(self.map_list)
        '''                       

class Chunks:

    def __init__(self, images):

        self.images = images

    def mountains(self, x, y, map_dic_XY, chunk, map_size):


        if chunk == 'sea':
            pass
            
        elif random.random() > 0.9:
            map_dic_XY[x,y] = { 'chunk' : 'mountain' }
                           
            mounVert = True
            mounHor = True
            while mounHor or mounVert:

                if random.random() > 0.8 and mounHor:
                    x = x + zoomv * random.randint(-1,1)
                    if x < 0:
                        x = 0
                    if x > map_size[0]:
                        x = map_size[0]
                    map_dic_XY[x,y] = { 'chunk' : 'mountain' }
                else:
                    mounHor = False
                if random.random() > 0.8 and mounVert:
                    y = y + zoomv * random.randint(-1,1)
                    if y < 0:
                        y = 0
                    if y > map_size[1]:
                        y = map_size[1]
                    map_dic_XY[x,y] = { 'chunk' : 'mountain' }
                else:
                    mounVert = False

        return map_dic_XY



    def randChunk(self, x, y, chunk, chunkOld, map_dic_XY):
        
        if random.random() > 0.9:
            dicChunk = { 'chunk' : chunk }
            map_dic_XY[x,y] = dicChunk
        else:  
            dicChunk = { 'chunk' : chunkOld }
            map_dic_XY[x,y] = dicChunk


        return map_dic_XY[x,y]


    def chooseChunk(self, map_list, images, tile, Chunk):

        chunk = map_list[tile]['chunk']

        if chunk == 'desert':

            return Chunk.desert(self.images)

        if chunk == 'sea':

            return Chunk.sea(self.images)

        if chunk == 'normal':

            return Chunk.normal(self.images)

        if chunk == 'mountain':

            return Chunk.mountain(self.images)

        if chunk == 'winter':

            return Chunk.winter(self.images)

        else:

            return Chunk.sea(self.images)


    def addChunk(self, chunkOld):

        chunkList = ('desert','winter','normal','sea','lakes')

        if random.random() > 0.5:

            chunk = chunkList[random.randint(0,len(chunkList)-1)]

        else:

            chunk = chunkOld

        return chunk

    def desert(self, images):
        prob = random.random()
        
        var = random.randint(0,len(self.images.keys())-1)
        cat = 'desert'

        var = random.randint(0,len(self.images[cat].keys())-1)
        grp = list(self.images[cat].keys())[var]

        var = random.randint(0, len(self.images[cat][grp])-1)
        img = var

        lista = (cat,grp,img)
        return lista

    def mountain(self, images):
        prob = random.random()
        
        var = random.randint(0,len(self.images.keys())-1)
        cat = 'mountains'

        var = random.randint(0,len(self.images[cat].keys())-1)
        grp = list(self.images[cat].keys())[var]

        var = random.randint(0, len(self.images[cat][grp])-1)
        img = var

        lista = (cat,grp,img)
        return lista

    def sea(self, images):
        prob = random.random()

        var = random.randint(0,len(self.images.keys())-1)
        cat = 'global'

        var = random.randint(0,len(self.images[cat].keys())-1)
        grp = 'sea'

        var = random.randint(0, len(self.images[cat][grp])-1)
        img = var

        lista = (cat,grp,img)
        return lista

    def normal(self, images):
        prob = random.random()
        
        var = random.randint(0,len(self.images.keys())-1)
        cat = 'normal'

        var = random.randint(0,len(self.images[cat].keys())-1)
        grp = list(self.images[cat].keys())[var]

        var = random.randint(0, len(self.images[cat][grp])-1)
        img = var

        lista = (cat,grp,img)
        return lista

    def winter(self, images):
        prob = random.random()
        
        var = random.randint(0,len(self.images.keys())-1)
        cat = 'winter'

        var = random.randint(0,len(self.images[cat].keys())-1)
        grp = list(self.images[cat].keys())[var]

        var = random.randint(0, len(self.images[cat][grp])-1)
        img = var

        lista = (cat,grp,img)
        return lista

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

    def tile(map_dic_XY, id):
        attributes = {'visible' : False, 'visibleBy' : 0}
        map_dic_XY[id] =  {'attributes' :  attributes}

class Tiles:

    
    def tileEdit(map_dic_XY, id, key, var):

        map_dic_XY[id]['attributes'][key] = var

    def tileEditArray(map_dic_XY, id, keys, vars):
        x = 0
        for key in keys:
            map_dic_XY[id]['attributes'][keys] = vars[x]
            var = var + 1

