import cocos
import pyglet
import random
import sys
import math

class Maze:
    def __init__(self):
        self.sprite=cocos.sprite.Sprite("resources/maze.png")
        self.sprite.position=270,270
        self.map= [
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

    def put(self,i,j,theObject):
        x,y=self.cell_center_position(i,j)
        if self.map[i][j]==0:
            self.map[i][j]=theObject
            theObject.sprite.x=x
            theObject.sprite.y=y

    def cell_center_position(self,i,j):
        return 30+60*j,30+60*(8-i)

    def theObject_in_cell(self,i,j):
        if i<0 or j<0 or i>8 or j>8:
            return None
        else:
            return self.map[i][j]

    def collision(self,theObject):
        x=theObject.sprite.x
        y=theObject.sprite.y
        i,j=self.in_the_cell(x,y)
        if i<0 or j<0 or i>8 or j>8:
            return True
        if self.map[i][j]!=0 and self.map[i][j]!=theObject:
            return True
        else:
            return False

    def in_the_cell(self,x,y):
        i=8-(y-30)//60
        j=(x-30)//60
        return i,j
