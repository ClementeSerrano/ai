#!/usr/bin/python
import cocos
import time
import pyglet
import random
import keyboard
import sys
import math
import pacman
import coordenadas
from enemigo import *


class Fantasma(Enemigo):
    def __init__(self,laberinto):
        self.atlas=pyglet.image.load("resources/fantasma.png")
        self.animaciones=pyglet.image.ImageGrid(self.atlas,1,16)
        self.frame=0
        self.sprite=cocos.sprite.Sprite(self.animaciones[self.frame])
        self.laberinto=laberinto
        self.movimientos=[[60,0],[0,60],[-60,0],[0,-60]]
        self.cont=0
        self.fantasma_x=3
        self.fantasma_y=4
        
        

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

    def mover_aleatorio(self):
        
        
        if keyboard.is_pressed('up'):
            print('KEY ARRIBA!')
            #p=self.laberinto.en_celda(self.sprite.x,self.sprite.y)
            #print("X:",p[0],"Y:",p[1])
            return
        if keyboard.is_pressed('down'):
            print('KEY ABAJO!')
            #p=self.laberinto.en_celda(self.sprite.x,self.sprite.y)
            #print("X:",p[0],"Y:",p[1])
            return
        if keyboard.is_pressed('left'): 
            print('KEY IZQUIERDA!')
            #p=self.laberinto.en_celda(self.sprite.x,self.sprite.y)
            #print("X:",p[0],"Y:",p[1])
            return
        if keyboard.is_pressed('right'):
            print('KEY DERECHA!')
            #p=self.laberinto.en_celda(self.sprite.x,self.sprite.y)
            #print("X:",p[0],"Y:",p[1])
            return
    
        #posiciones=list(range(0,len(self.movimientos)))
        if(len(coordenadas.aux_coord)!=0):
            largo = len(coordenadas.aux_coord)
            print("largo",largo)
            print("CONT",self.cont)
            if(self.cont==largo):
                p=self.laberinto.en_celda(self.sprite.x,self.sprite.y)
                self.fantasma_x=p[0]
                self.fantasma_y=p[1]
                self.cont=0
                return
            while(self.cont<largo):
                
                movimiento=[]
                
                if coordenadas.aux_coord[self.cont]=="arriba":
                    movimiento.append(0)
                    movimiento.append(60)
                    #print("movimiento arriba")
                
                if coordenadas.aux_coord[self.cont]=="abajo":
                    movimiento.append(0)
                    movimiento.append(-60)
                    #print("movimiento abajo")
                    
                if coordenadas.aux_coord[self.cont]=="izquierda":
                    movimiento.append(-60)
                    movimiento.append(0)
                    #print("movimiento izquierda")
                
                if coordenadas.aux_coord[self.cont]=="derecha":
                    movimiento.append(60)
                    movimiento.append(0)
                    #print("movimiento derecha")
                if self.movimiento_posible(movimiento):
                    self.mover(movimiento)
                    self.cont+=1
                    print("CONTADOR",self.cont)
                    return
                            
                    
                    
                    
                        
            '''while len(posiciones)>0:
                i=random.choice(posiciones)
            
                
                #print("coooord",coordenadas.aux_coord)
                    #print("SOY EL FANTASMA\nCOORD",coord)
                posiciones.remove(i)
                movimiento=self.movimientos[i]
                print("movimientos",movimiento)
                #print("movimiento",movimiento)
                if self.movimiento_posible(movimiento):
                    
                    self.mover(movimiento)
                    return'''
        
    def mover(self,movimiento):
        p=self.laberinto.en_celda(self.sprite.x,self.sprite.y)
        #print("P !",p)
        
        #print("movimiento x",movimiento[0])
        #print("movimiento y",movimiento[1])
        self.laberinto.mapa[p[0]][p[1]]=0
       
        self.sprite.x+=movimiento[0]
        self.sprite.y+=movimiento[1]
        p=self.laberinto.en_celda(self.sprite.x,self.sprite.y)
        #print("SOY EL FANTASMA P",p)
        self.laberinto.mapa[p[0]][p[1]]=self
        
        
