from src.UnitsNS import Unit, Armies


class UnitsCreators:

    #attributes = {'damage' : , 'vision' :}
    #image = {'imgCat' : , 'imgGrp' : , 'img' :}
    #unit = Unit(name, image, movReg, attributes, self.units, id)
    #self.untisObj[] = unit

    def __init__(self, variables):

        self.units = {}
        self.armies = {}
        self.Armies = Armies()
        

    def create_units(self, images):  

        attributes = {'damage' : 10, 'vision' : 5}
        image = {'imgCat' : 'Units', 'imgGrp' : 'Units', 'img' : 'Soldier.jpg'}
        unit = Unit('soldado con lanza', image, 'land', attributes, self.units, '00')


    def create_army(self, x, y, maps, player, unitDic, Armies, units = {None}):

        id = 'army.' + str(len(self.Armies.armiesInGame.keys))
        army = self.Armies.create_army(x, y, width, height, id, self.armies, unitsDic, self.Armies, maps, player, None, units)

    def delete_army(self, id):
        self.Armies.army_erase(id)

