import pygame
from player import player

#créer une seconde classe qui va representer notre jeu
class game:
    
    def __init__(self):
        #generer notre joueur
        self.player = player()
        self.pressed = {}