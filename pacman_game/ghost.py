import cocos
import pyglet
import random
import sys
import math
import pacman
import astart
from enemy import *

class Ghost(Enemy):
    def __init__(self,maze):
        self.atlas=pyglet.image.load("resources/ghost.png")
        self.animations=pyglet.image.ImageGrid(self.atlas,1,16)
        self.frame=0
        self.sprite=cocos.sprite.Sprite(self.animations[self.frame])
        self.maze=maze
        self.movements=[[60,0],[0,60],[-60,0],[0,-60]]
        self.ghost_x=3
        self.ghost_y=4

    def animar(self,px,py):
        self.frame+=1
        self.frame%=2
        self.sprite.image=self.animations[self.frame]
        self.random_move(px,py)

    def possible_movement(self,movement):
        self.sprite.x+=movement[0]
        self.sprite.y+=movement[1]
        if self.maze.collision(self):
            i,j=self.maze.in_the_cell(self.sprite.x,self.sprite.y)
            theObject=self.maze.theObject_in_cell(i,j)
            self.sprite.x-=movement[0]
            self.sprite.y-=movement[1]
            if isinstance(theObject,pacman.Pacman):
                print("I found you! :)")
                theObject.home()
                return True
            else:
                return False
        else:
            self.sprite.x-=movement[0]
            self.sprite.y-=movement[1]
            return True

    def random_move(self,px,py):
        pacman_x,pacman_y=self.maze.in_the_cell(px,py)
        if(pacman_y>=0 and pacman_x>=0):
            if(astart.astar((self.ghost_x, self.ghost_y),(pacman_x,pacman_y))):
                theArray=[]
                theArray+=astart.astar((self.ghost_x, self.ghost_y),(pacman_x,pacman_y))
                theArray.reverse()
                print(theArray)
                initial=[(self.ghost_x,self.ghost_y)]
                movement=[]
                possible_movements=[(0,1),(0,-1),(1,0),(-1,0)]
                for a in range(len(theArray)):
                    l=[] #empty list to determine the movement
                    for i in range(2):
                        if(i==0):
                            row=theArray[a][i] 
                        else:
                            col=theArray[a][i]
                    l.append((row,col)) 
                    #right 
                    if((tuple(map(sum, zip(initial[0], possible_movements[0]))))==l[0]):
                        movement.append(60)
                        movement.append(0)
                    #left
                    if((tuple(map(sum, zip(initial[0], possible_movements[1]))))==l[0]):
                        movement.append(-60)
                        movement.append(0)
                    #down
                    if((tuple(map(sum, zip(initial[0], possible_movements[2]))))==l[0]):
                         movement.append(0)
                         movement.append(-60)
                    #up
                    if((tuple(map(sum, zip(initial[0], possible_movements[3]))))==l[0]):
                        movement.append(0)
                        movement.append(60)
                    initial=[]
                    initial.append(theArray[a])
                    if(self.possible_movement(movement)):
                        self.ghost_x,self.ghost_y=self.move(movement)
                    return

    def move(self,movement):
        p=self.maze.in_the_cell(self.sprite.x,self.sprite.y)
        self.maze.map[p[0]][p[1]]=0
        self.sprite.x+=movement[0]
        self.sprite.y+=movement[1]
        p=self.maze.in_the_cell(self.sprite.x,self.sprite.y)
        self.maze.map[p[0]][p[1]]=self
        self.ghost_x=p[0]
        self.ghost_y=p[1]
        return self.ghost_x,self.ghost_y
