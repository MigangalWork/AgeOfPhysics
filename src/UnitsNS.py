import pygame

units = {}

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

class Unit:

    def __init__(self, name, image, movReg, attributes, units, id):
        
        self.name = name
        self.image = image
        self.attributes = daño
        self.movReg = movReg
        self.id = id
        units[id] = self
        

    def unitAddToArmy(self): 
        Menus.menuAdd(self.x, self.y, self.width, self.height, self.id) 

class UnitInArmy(Unit):

    def __init__(self, units, army, id):

        self.name = units.name
        self.image = units.image
        self.attributes = units.attributes
        self.movReg = units.movReg
        self.id = id
        self.armyId = army.id
        self.unitId = units.id



class Army:

    def __init__(self, x, y, width, height, id, armies, unitsDic, armiesGen, maps, player, image=None, units={None}):

            self.x = x
            self.y = y
            self.id = id
            if image == None:
                self.width = width
                self.height =  height
            else:
                self.width = image.get_width()
                self.height =  image.get_height()

            self.units = units
            self.armyImgSize = len(self.units)//5
            self.screen = armiesGen.armyCheckScreen(self.units, maps, unitsDic)

            self.player = player
            
            
            armies[id] = self
            armiesGen.numberOfArmies = armiesGen.numberOfArmies + 1

            armiesGen.Armies.armyAdd(self.x, self.y, self.image, self.id)

    def addUnitToArmy(self, key, num = 1, Units): 
        
        if key in self.units.keys():

            self.units[key] = 
        
        else:

            self.units[key]

    def getGeneralStats():

        pass

    def addArmyAttribute():

        pass



class Armies:

    def __init__(self):

        self.numberOfArmies = 0
        self.armiesInGame = {}
        self.armies = {}

        

    def army_clicked(self, xy):
        for key in self.armiesInGame.keys():
            
            if self.armiesInGame[key].collidepoint(xy):
                
                return key
        return '-1'

    def armyAdd(self, x, y, width, height, id):

        army = pygame.Rect((x, y, width, height))
        self.armiesInGame[id] = army

    
    def armyErase(self, id):
        del self.armiesInGame[id]

    def armyDraw(self, variables, players=None):
        zoomv = variables['zoomv']
        for key in self.armiesInGame.keys():
            x = armies[key].x
            y = armies[key].y
            width = zoomv # + armies[key].armyImgSize
            height = zoomv # + armies[key].armyImgSize
            screen = armies[key].screen
            pygame.draw.rect(screen, (0, 0, 0), (x,y,width, height))
            #pygame.draw.rect(screen, players[id]['color'], (x-1,y-1,width+2, height)+2, 2)
    
    def armyCheckScreen(self, units, maps, unitsDic):
        
        for i in units:
            if 'land' or 'sea' in unitsDic[i]['movReg']:
                return maps[0]
            elif 'air' in unitsDic[i]['movReg']:
                return maps[1]
            elif 'space' in unitsDic[i]['movReg']:
                return maps[2]
            else:
                return supmapa

    def armyUpdate(self, movex, movey, zoomv, armies):

        for key in self.armiesInGame.keys():
            armies[key]['x'] = armies[key]['x'] - movex
            armies[key]['y'] = armies[key]['y'] - movey
            armies[key]['armyImgSize'] = armies[key]['armyImgSize'] + zoomv



    def armyReturn(self):
        return self.numberOfArmies, self.armiesInGame

    def create_army(self, x, y, width, height, id, zoomv, armiesGen, maps, player, image=None, units={None}):

        army = Amry(x, y, width, height, id, self.armies, unitsDic, zoomv, armiesGen, maps, player)


        
        