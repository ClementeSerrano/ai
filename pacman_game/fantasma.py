import cocos
import pyglet
import random
import sys
import math
import pacman
from pacman import *
from enemigo import *

class Fantasma(Enemigo):
    def __init__(self,laberinto):
        self.atlas=pyglet.image.load("resources/fantasma.png")
        self.animaciones=pyglet.image.ImageGrid(self.atlas,1,16)
        self.frame=0
        self.sprite=cocos.sprite.Sprite(self.animaciones[self.frame])
        self.laberinto=laberinto
        self.movimientos=[[60,0],[0,60],[-60,0],[0,-60]]

    def animar(self,px,py):
        self.frame+=1
        self.frame%=2
        self.sprite.image=self.animaciones[self.frame]
        self.mover_aleatorio()

    def movimiento_posible(self,movimiento):
        self.sprite.x+=movimiento[0]
        self.sprite.y+=movimiento[1]
        if self.laberinto.colision(self):
            i,j=self.laberinto.en_celda(self.sprite.x,self.sprite.y)
            objeto=self.laberinto.objeto_en_celda(i,j)
            self.sprite.x-=movimiento[0]
            self.sprite.y-=movimiento[1]
            if isinstance(objeto,Pacman):
                print("te pille")
                objeto.home()
                return True
            else:
                return False
        else:
            self.sprite.x-=movimiento[0]
            self.sprite.y-=movimiento[1]
            return True

    def mover_aleatorio(self):
        posiciones=list(range(0,len(self.movimientos)))
            
        while len(posiciones)>0:
            i=random.choice(posiciones)
            
            posiciones.remove(i)
            movimiento=self.movimientos[i]
            #print("movimiento",movimiento)
            if self.movimiento_posible(movimiento):
                self.mover(movimiento)
                return
        
    def mover(self,movimiento):
        p=self.laberinto.en_celda(self.sprite.x,self.sprite.y)
        #print("P !",p)
        #print("SOY EL FANTASMA\nCOORD",pacman.coord)
        #print("movimiento x",movimiento[0])
        #print("movimiento y",movimiento[1])
        self.laberinto.mapa[p[0]][p[1]]=0
        self.sprite.x+=movimiento[0]
        self.sprite.y+=movimiento[1]
        p=self.laberinto.en_celda(self.sprite.x,self.sprite.y)
        #print("SOY EL FANTASMA P",p)
        self.laberinto.mapa[p[0]][p[1]]=self
