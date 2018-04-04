import cocos
import pyglet
import random
import sys
import math
import fantasma
from comida import *
from enemigo import *

class Pacman:
    def __init__(self,laberinto):
        self.atlas=pyglet.image.load("resources/pacman.png")
        self.animaciones=pyglet.image.ImageGrid(self.atlas,1,16)
        self.frame=0
        self.sprite=cocos.sprite.Sprite(self.animaciones[self.frame])
        self.vidas=3
        self.laberinto=laberinto
        self.puntaje=0
        self.pacman_posicion=[]

    def home(self):
        p=self.laberinto.en_celda(self.sprite.x,self.sprite.y)
        self.laberinto.mapa[p[0]][p[1]]=0
        x,y=self.laberinto.posicion_centro_celda(0,0)
        self.sprite.x=x
        self.sprite.y=y
        self.laberinto.mapa[0][0]=self

    def mover(self,dx,dy):
        self.frame+=1
        if self.frame>2:
            self.frame=0
        self.sprite.image=self.animaciones[self.frame]
        ox=self.sprite.x
        oy=self.sprite.y
        self.sprite.x+=dx
        self.sprite.y+=dy

        if ox<self.sprite.x:
            self.sprite.rotation=180
        else:
            self.sprite.rotation=0
        if oy<self.sprite.y:
            self.sprite.rotation=90
        elif oy>self.sprite.y:
            self.sprite.rotation=270
        p=self.laberinto.en_celda(self.sprite.x,self.sprite.y)
        self.pacman_posicion=[]
        self.pacman_posicion.append(p[0])
        self.pacman_posicion.append(p[1])
        #fan=fantasma.Fantasma(self.laberinto)
       
        if(self.laberinto.colision(self)):
            i,j=self.laberinto.en_celda(self.sprite.x,self.sprite.y)
            objeto=self.laberinto.objeto_en_celda(i,j)
            if isinstance(objeto,Comida):
                objeto.sprite.opacity=0
                self.puntaje+=objeto.puntos
                self.laberinto.mapa[i][j]=0
            elif isinstance(objeto,Enemigo):
                print("choque con un fantasma")
                self.sprite.x=ox
                self.sprite.y=oy
                self.home()
            else:
                self.sprite.x-=dx
                self.sprite.y-=dy
        else:
            p=self.laberinto.en_celda(ox,oy)
            self.laberinto.mapa[p[0]][p[1]]=0
            p=self.laberinto.en_celda(self.sprite.x,self.sprite.y)
            self.laberinto.mapa[p[0]][p[1]]=self
