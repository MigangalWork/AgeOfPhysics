import pygame
from VariablesGlobales import *


class genMap:
    
    def genMap():
        global mapDic, tilesInMap
        mapDic = {}
        tilesInMap = 0
        for i in range (map_sizex[0], map_size[0], zoomv):
            for j in range (map_sizey[0], map_size[1], zoomv):
                
                mapDic[tilesInMap] = {'img' : random.randint(0,4), 'pos' : (i,j)}
                mapDicXY[i,j] = {'img' : mapDic[tilesInMap], 'pos' : tilesInMap}
                tilesInMap = tilesInMap + 1

    def zoomMap():

        global mapDic
        var = 0
        for i in range (map_sizex[0], map_size[0], zoomv):
            for j in range (map_sizey[0], map_size[1], zoomv):
                
                mapDic[var]['pos'] = (i,j)
                var = var + 1
        
        #for i in range(tilesInMap):
        #    mapDic[var]['pos']      

    def editMap(i, j, var):
        global mapDic
        global mapTile
        mapDic[i]['img'] = var
        #mapTile[i,j]['img'] = var


class Mapa:
    def __init__(self, imgsize):
        self.imgsize = imgsize

    def create(self):
        
        for i in range (tilesInMap):
            #print(i)
            supmapa.blit(base_image[mapDic[i]['img']][zoomv],(mapDic[i]['pos']))        