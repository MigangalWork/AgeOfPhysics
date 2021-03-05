import pygame, sys, random, ctypes
import logging
logging.getLogger().setLevel(logging.INFO)

from src.config import startConfig
from src.Map import GenMap, Mapa, Tiles, Chunks
from src.Menus import Menus, Buttons
from src import utils
from src.Text import Text
from src.Mouse import  draw_select_multi, Border, Mouse, Zooms
from src.GameObjets.ButtonsAndMenus import MenuCreators, Menus, Buttons
from src.Display import Display
from src.Events.Keyboard import Keyboard
from src.Events.MouseInput import MouseInput

import yaml


class players:

    def __init__(self):

        self.players = {}




class player:

    __init__(self, name, players):
     
    self.name = name
    self.id = id

    players[id] = self