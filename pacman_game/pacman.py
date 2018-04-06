import cocos
import pyglet
import random
import sys
import math
import ghost
from food import *
from enemy import *

class Pacman:
    def __init__(self,maze):
        self.atlas=pyglet.image.load("resources/pacman.png")
        self.animations=pyglet.image.ImageGrid(self.atlas,1,16)
        self.frame=0
        self.sprite=cocos.sprite.Sprite(self.animations[self.frame])
        self.lifes=3
        self.maze=maze
        self.score=0

    def home(self):
        p=self.maze.in_the_cell(self.sprite.x,self.sprite.y)
        self.maze.map[p[0]][p[1]]=0
        x,y=self.maze.cell_center_position(0,0)
        self.sprite.x=x
        self.sprite.y=y
        self.maze.map[0][0]=self

    def move(self,dx,dy):
        self.frame+=1
        if self.frame>2:
            self.frame=0
        self.sprite.image=self.animations[self.frame]
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
        p=self.maze.in_the_cell(self.sprite.x,self.sprite.y)
       
        if(self.maze.collision(self)):
            i,j=self.maze.in_the_cell(self.sprite.x,self.sprite.y)
            theObject=self.maze.theObject_in_cell(i,j)
            if isinstance(theObject,Food):
                theObject.sprite.opacity=0
                self.score+=theObject.score
                self.maze.map[i][j]=0
            elif isinstance(theObject,Enemy):
                print("I clash with a ghost!")
                self.sprite.x=ox
                self.sprite.y=oy
                self.home()
            else:
                self.sprite.x-=dx
                self.sprite.y-=dy
        else:
            p=self.maze.in_the_cell(ox,oy)
            self.maze.map[p[0]][p[1]]=0
            p=self.maze.in_the_cell(self.sprite.x,self.sprite.y)
            self.maze.map[p[0]][p[1]]=self
