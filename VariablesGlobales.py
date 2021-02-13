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
screen_size = (1000,1000)

mapa = {}
zoomv = 10
zoomvBase = 10

zoomList = [zoomv, zoomv*2, zoomv*4, zoomv*8, zoomv*16]

clicking = {}

map_sizex = [0,100] 
map_sizey = [0,100] 

map_size = [map_sizex[1],map_sizey[1]]


imagen = {0 : "images/image1.png", 1 : "images/image2.png"}

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

print                       (base_image)            #:D

mapDic = {}
mapTile = {}

selected = []

selectedM = {}

untisDic = {}