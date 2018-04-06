import cocos
import pyglet
import random
import sys
import math

class Food:
    def __init__(self,typeOf,bonus,score,image):
        self.typeOf=typeOf
        self.bonus=bonus
        self.score=score
        self.sprite=cocos.sprite.Sprite(image)
