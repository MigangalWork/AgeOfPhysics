import pygame

class Units:

    def unitClicked(xy):
        for i in range(0,len(armiesInGame)):
            key = list(armiesInGame.keys())[i]
            if armiesInGame[key].collidepoint(xy):
                
                return key
        return -1

    def unitAdd(x,y,image,id):
        global menusActivos
        menu = pygame.image.get_rect((x, y, width, height))
        menu.rect.center 
        menusActivos[id] = menu
        print(menusActivos)
    
    def unitErase(id):
        del unitsActivas[id]

    def unitDraw(menus):
        for key in unitsActivas.keys:

            x = menus[key]['x']
            y = menus[key]['y']
            width = menus[key]['width']
            height = menus[key]['height']
            screen = menus[key]['screen']
            #pantallita.blit(key, (0,0))

            pygame.draw.rect(screen, (0, 0, 0), (x,y,width, height))

class Unit:

    def __init__(self, name, image, movReg, attributes, id):
        
        self.name = name
        self.image = image
        self.attributes = attributes
        self.movReg = movReg
        self.id = id
        units[id] = {'name' : self.name, 'image' : self.image, 'movReg' : self.movReg, 'attributes' : self.attributes}
        

    def activateUnit(self): 
        Menus.menuAdd(self.x, self.y, self.width, self.height, self.id) 


class army:

    def __init__(self, x, y, id, units={}, armies, zoomv, armiesGen, maps):

            self.x = x
            self.y = y
            self.id = id


            self.zoom = zoomv
            self.units = units
            self.armyImgSize = zoomv * len(self.units)//5
            self.screen = armiesGen.armyCheckScreen(maps)
            
            armies[id] = {'x' : self.x, 'y' : self.y, 'screen' : self.screen, 'armyImgSize' : self.armyImgSize, 'id' : self.id, 'units' : self.units}
            armiesGen.numberOfArmies = armiesGen.numberOfArmies + 1


class Armies:

    def __init__(self):
        self.numberOfArmies = 0
        self.armiesInGame = {}

        

    def armyClicked(self, xy):
        for key in self.armiesInGame.keys:
            
            if self.armiesInGame[key].collidepoint(xy):
                
                return key
        return -1

    def armytAdd(self, x,y,image,id):

        army = pygame.Rect((x, y, width, height))
        self.armiesInGame[id] = army

    
    def armyErase(self, id):
        del self.armiesInGame[id]

    def armyDraw(self, armies):
        for key in self.armiesInGame.keys():
            x = armies[key]['x']
            y = armies[key]['y']
            width = armies[key]['armyImgSize']
            height = armies[key]['armyImgSize']
            screen = armies[key]['screen']
            pygame.draw.rect(screen, (0, 0, 0), (x,y,width, height))
    
    def armyCheckScreen(self, maps):
        
        for i in self.units:
            if 'land' or 'sea' in self.units[i]['movReg']:
                self.screen = maps[0]
            elif 'air' in self.units[i]['movReg']:
                self.screen = maps[1]
            elif 'space' in self.units[i]['movReg']:
                self.screen = maps[2]
            else:
                self.screen = supmapa

    def armyUpdate(self, movex, movey, zoomv, armies)

        for key in self.armiesInGame.keys():
            armies[key]['x'] = armies[key]['x'] - movex
            armies[key]['y'] = armies[key]['y'] - movey
            armies[key]['armyImgSize'] = armies[key]['armyImgSize'] + zoomv



    def armyReturn():
        return self.numberOfArmies, self.armiesInGame

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
        
        