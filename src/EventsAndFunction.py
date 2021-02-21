import pygame

class EventsFinder:

    def findFunction(key, display):
        
        if key == 'I0000':
             
             EventsFunctions.startGame(display)



class EventsFunctions:

    def startGame(display):
        from main import Game, MainMenu, variables, menu_creator
        from ButtonsAndMenus import MenuCreators
        print(display)
        print(variables)
        print('adios')
        
        Game.play(variables, display)

