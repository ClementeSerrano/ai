import cocos
import pyglet
import random
import sys
import math

class Comida:
    def __init__(self,tipo,bonus,puntos,imagen):
        self.tipo=tipo
        self.bonus=bonus
        self.puntos=puntos
        self.sprite=cocos.sprite.Sprite(imagen)
