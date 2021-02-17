import pygame, sys, random, ctypes

pygame.init()

fps = 60

run = True
white = (255,255,255)
negro = (0,0,0)
movex = 0
movey = 0
sizex = 0
sizey = 0
screen_size = (500,500)

mapa = {}
zoomv = 10
zoomvBase = 10

zoomList = [zoomv, zoomv*2, zoomv*4, zoomv*8, zoomv*16]

clicking = {1 : False}

map_sizex = [0,500] 
map_sizey = [0,500] 

map_size = [map_sizex[1],map_sizey[1]]
tilesInMap = 0

imagen = {0 : "images/grass1.png", 1 : "images/grass2.png", 2 : "images/grass1.png", 3 : "images/floor1.jpg", 4 : "images/floor2.jpg", 5 : "images/city.jpg"}

base_image = {}
class sizemap:
    def sizemap(imgsize, base_image):
        red_image = pygame.transform.scale(base_image, (imgsize, imgsize))
        return red_image

for image in range(len(imagen.keys())):
    baseImage = pygame.image.load(imagen[image])
    base_image[image] = {}
    
    for size in zoomList:
        base_image[image][size] = sizemap.sizemap(size,baseImage)



mapDic = {}
mapDicXY = {}
mapTile = {}



#Raton

clicked = [0, 0]
clickedMap = [0, 0]
clickedMapOrigin = [0, 0]
unClicked = []
unClickedMap = []
selected = []
baseEleccion = []
selectedM = {}

untisDic = {}

vel_mov_mapa = [1, 1]

#menus

menus = {}
menusActivos = {}

#buttons

buttons = {}
buttonsActivos = {}

#Unidades

units = {}
unitsInGame = {}
armiesInGame = []
numberOfArmies = 0

#Texto

textActive = False
