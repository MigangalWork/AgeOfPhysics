import pygame


class EventsFinder:

    def findFunction(key, variables, constructors, superficies):
        

        keyList = key.split('.')
        

        if key == 'I0000':
             
             EventsFunctions.startGame(variables, constructors, superficies)
        
        if key == 'I0010':

            variables['text_active'] = 'T'+key


        if keyList[0] == 'army':

            EventsFunctions.armySelected(keyList, variables)
        
        if key == '0000':

            #EventsFunctions.createArmy(variables, constructors)
            EventsFunctions.closeGame()








class EventsFunctions:

    def startGame(variables, constructors, superficies):
        from src.Game import Game
        constructors['menu_creator'].delete_menus('I00')
        Game.play(variables, constructors, superficies)

    def armySelected(keyList, variables):
        from src.Units import Armies
        variables['armySelected'] = True

    def createArmyPick(variables, constructors):
        
        variables['UnitsCreator'].create_army(variables['clicked'][0], variables['clicked'][1], variables['zoomv'], variable['maps'], 'player_1', variables['UnitsCreator'].units, variables['Armies'], None)

    def closeGame():

        import sys
        sys.exit()




