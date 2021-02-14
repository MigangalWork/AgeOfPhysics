from VariablesGlobales import *

class Units:

    def unitClicked(xy):
        for i in range(0,len(unitsActivas)):
            key = list(unitsActivas.keys())[i]
            if unitsActivas[key].collidepoint(xy):
                
                return True
        return False

    def unitAdd(x,y,width,height,id):
        global menusActivos
        menu = pygame.Rect((x, y, width, height))
        menusActivos[id] = menu
        print(menusActivos)
    
    def unitErase(id):
        del unitsActivas[id]

    def unitDraw():
        for i in range(0,len(unitsActivas)):
            #myIter = iter(menusActivos) no se como usarlo pero es significativamente mas eficiente y nos vendira bien
            #key = next(myIter)
            key = list(menusActivos.keys())[i]
            x = menus[key]['x']
            y = menus[key]['y']
            width = menus[key]['width']
            height = menus[key]['height']
            screen = menus[key]['screen']
            #pantallita.blit(key, (0,0))

            pygame.draw.rect(screen, (0, 0, 0), (x,y,width, height))

class Unit:

    def __init__(self, name, image, attributes, id):
        global menus
        self.name = name
        self.image = image
        self.attributes = attributes
        self.id = id
        units[id] = {'name' : self.name, 'image' : self.image, 'attributes' : self.attributes}
        #self.surface = pygame.Surface((x,y))


    def activateUnit(self): 
        Menus.menuAdd(self.x, self.y, self.width, self.height, self.id) 


class army:

    def __init__(self, x, y, id):

            self.x = x
            self.y = y
            self.id = id

            self.image = units[self.id]['image'][zoomv]
            self.zoom = zoomv
            self.rect = self.image.get_rect()
            self.rect.center = (x,y)

            armiesInGame[id] = {'x' : self.name, 'y' : self.image, 'id' : self.id}
            numberOfArmies = numberOfArmies + 1

class UnitInGame(Unit):

    def __init__(self, x, y, id):

        self.x = x
        self.y = y
        self.id = id

        self.image = units[self.id]['image'][zoomv]
        self.zoom = zoomv
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

        unitsInGame[id] = {'x' : self.name, 'y' : self.image, 'id' : self.id}
        
        