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
screen_size = (100,100)

mapa = {}
zoomv = 5


map_sizex = [0,100] 
map_sizey = [0,100] 

map_size = [map_sizex[1],map_sizey[1]]


imagen = {0 : "images/image1.png", 1 : "images/image2.png"}

base_image = {}

for i in (0,1):
    base_image[i] = pygame.image.load(imagen[i])



mapDic = {}
mapTile = {}

selected = []

selectedM = {}