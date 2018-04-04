import cocos
import pyglet
import random
import sys
import math
import pacman
import astart
#from pacman import *
from enemigo import *

class Fantasma(Enemigo):
    def __init__(self,laberinto):
        self.atlas=pyglet.image.load("resources/fantasma.png")
        self.animaciones=pyglet.image.ImageGrid(self.atlas,1,16)
        self.frame=0
        self.sprite=cocos.sprite.Sprite(self.animaciones[self.frame])
        self.laberinto=laberinto
        self.movimientos=[[60,0],[0,60],[-60,0],[0,-60]]
        self.fantasma_x=3
        self.fantasma_y=4
        self.cont=0

    def animar(self,px,py):
        self.frame+=1
        self.frame%=2
        self.sprite.image=self.animaciones[self.frame]
        self.mover_aleatorio(px,py)

    def movimiento_posible(self,movimiento):
        self.sprite.x+=movimiento[0]
        self.sprite.y+=movimiento[1]
        if self.laberinto.colision(self):
            i,j=self.laberinto.en_celda(self.sprite.x,self.sprite.y)
            objeto=self.laberinto.objeto_en_celda(i,j)
            self.sprite.x-=movimiento[0]
            self.sprite.y-=movimiento[1]
            if isinstance(objeto,pacman.Pacman):
                print("te pille")
                objeto.home()
                return True
            else:
                return False
        else:
            self.sprite.x-=movimiento[0]
            self.sprite.y-=movimiento[1]
            return True

    def mover_aleatorio(self,px,py):
        pacman_x=0
        pacman_y=0
        pacman_x,pacman_y=self.laberinto.en_celda(px,py)
        if(pacman_y!=0 and pacman_x!=0):
            if(astart.astar((self.fantasma_x, self.fantasma_y),(pacman_x,pacman_y))):
                arreglo=[]
                arreglo+=astart.astar((self.fantasma_x, self.fantasma_y),(pacman_x,pacman_y))
                arreglo.reverse()
                inicial=[(self.fantasma_x,self.fantasma_y)]
                movimiento=[]
                movimientos_posibles=[(0,1),(0,-1),(1,0),(-1,0)]
                for a in range(len(arreglo)):
                    l=[] # lista vacia para determinar el movimiento
                    for i in range(2):
                        if(i==0):
                            row=arreglo[a][i]
                            
                        else:
                            col=arreglo[a][i]
                    l.append((row,col)) 
                    #derecha 
                    if((tuple(map(sum, zip(inicial[0], movimientos_posibles[0]))))==l[0]):
                        movimiento.append(60)
                        movimiento.append(0)
                    #izquierda
                    if((tuple(map(sum, zip(inicial[0], movimientos_posibles[1]))))==l[0]):
                        movimiento.append(-60)
                        movimiento.append(0)
                    #abajo
                    if((tuple(map(sum, zip(inicial[0], movimientos_posibles[2]))))==l[0]):
                         movimiento.append(0)
                         movimiento.append(-60)
                    #arriba
                    if((tuple(map(sum, zip(inicial[0], movimientos_posibles[3]))))==l[0]):
                        movimiento.append(0)
                        movimiento.append(60)
                    inicial=[]
                    inicial.append(arreglo[a])
                    if(self.movimiento_posible(movimiento)):
                        self.fantasma_x,self.fantasma_y=self.mover(movimiento)
                    
                    return       
        
           
           
        

    def mover(self,movimiento):
        p=self.laberinto.en_celda(self.sprite.x,self.sprite.y)
        self.laberinto.mapa[p[0]][p[1]]=0
        self.sprite.x+=movimiento[0]
        self.sprite.y+=movimiento[1]
        p=self.laberinto.en_celda(self.sprite.x,self.sprite.y)
        self.laberinto.mapa[p[0]][p[1]]=self
        self.fantasma_x=p[0]
        self.fantasma_y=p[1]
        return self.fantasma_x,self.fantasma_y
