import pygame

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
map_size = [100,100]

map_sizex = [0,50] 
map_sizey = [0,50] 


imagen = ("images/image1.png", "images/image2.png")

base_image = pygame.image.load(imagen[0])

base_image2 = pygame.image.load(imagen[1])

mapDic = {}

selected = []

selectedM = {}