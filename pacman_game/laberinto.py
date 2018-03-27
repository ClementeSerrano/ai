import cocos
import pyglet
import random
import sys
import math

class Laberinto:
    def __init__(self):
        self.sprite=cocos.sprite.Sprite("resources/laberinto.png")
        self.sprite.position=270,270
        self.mapa= [
            [0,0,0,0,0,0,0,0,0],
            [0,1,0,1,1,1,0,1,0],
            [0,0,0,0,0,0,0,0,0],
            [1,1,0,1,0,1,0,1,1],
            [0,1,0,1,1,1,0,1,0],
            [0,1,0,0,0,0,0,1,0],
            [0,0,0,1,1,1,0,0,0],
            [0,1,0,1,0,1,0,1,0],
            [0,0,0,0,0,0,0,0,0]
        ]

    def posicionar(self,i,j,objeto):
        x,y=self.posicion_centro_celda(i,j)
        if self.mapa[i][j]==0:
            self.mapa[i][j]=objeto
            objeto.sprite.x=x
            objeto.sprite.y=y

    def posicion_centro_celda(self,i,j):
        return 30+60*j,30+60*(8-i)

    def objeto_en_celda(self,i,j):
        if i<0 or j<0 or i>8 or j>8:
            return None
        else:
            return self.mapa[i][j]

    def colision(self,objeto):
        x=objeto.sprite.x
        y=objeto.sprite.y
        i,j=self.en_celda(x,y)
        if i<0 or j<0 or i>8 or j>8:
            return True
        if self.mapa[i][j]!=0 and self.mapa[i][j]!=objeto:
            return True
        else:
            return False

    def en_celda(self,x,y):
        i=8-(y-30)//60
        j=(x-30)//60
        return i,j
