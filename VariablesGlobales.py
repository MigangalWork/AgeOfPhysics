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
zoomv = 5


map_sizex = [0,200] 
map_sizey = [0,200] 

map_size = [map_sizex[1],map_sizey[1]]


imagen = {0 : "images/image1.png", 1 : "images/image2.png"}

base_image = {}

for i in range(len(imagen.keys())):
    base_image[i] = pygame.image.load(imagen[i])



mapDic = {}
mapTile = {}

selected = []

selectedM = {}