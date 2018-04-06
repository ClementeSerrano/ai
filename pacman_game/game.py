import cocos
import pyglet
import random
import sys
import math
from maze import *
from pacman import *
from ghost import *
from food import *

class PacmanGame(cocos.layer.Layer):
    is_event_handler=True

    def __init__(self):
        super(PacmanGame, self ).__init__()
        self.maze=Maze()

        self.pacman=Pacman(self.maze)
        x,y=self.maze.cell_center_position(5,4)
        self.pacman.sprite.x=x
        self.pacman.sprite.y=y

        self.atlas_items=pyglet.image.load("resources/food.png")
        self.image_item=pyglet.image.ImageGrid(self.atlas_items,1,16)

        self.ghost1=Ghost(self.maze)
        x,y=self.maze.cell_center_position(3,4)
        self.ghost1.sprite.x=x
        self.ghost1.sprite.y=y

        self.food0=Food(0,False,10,self.image_item[0])
        self.maze.put(8,0,self.food0)

        self.food1=Food(1,False,20,self.image_item[1])
        self.maze.put(0,8,self.food1)

        self.score=0
        self.marker_tag=cocos.text.Label("Score:",(190,450),font_size=16,bold=True)
        self.maker=cocos.text.Label(str(self.score).zfill(2),(270,450),font_size=16,bold=True)

        self.add(self.maze.sprite,z=0)
        self.add(self.pacman.sprite,z=1)
        self.add(self.ghost1.sprite,z=1)
        self.add(self.food0.sprite,z=1)
        self.add(self.food1.sprite,z=1)
        self.add(self.marker_tag,z=1)
        self.add(self.maker,z=1)
        self.schedule_interval(self.simulate,0.5)

    def simulate(self,*args,**kwargs):
        self.maker.element.text=str(self.pacman.score).zfill(2)
        self.ghost1.animar(self.pacman.sprite.x,self.pacman.sprite.y)

    def on_key_press(self, symbol, modifiers):
        if symbol == pyglet.window.key.RIGHT:
            self.pacman.move(60,0)
        elif symbol == pyglet.window.key.LEFT:
            self.pacman.move(-60,0)
        elif symbol == pyglet.window.key.UP:
            self.pacman.move(0,60)
        elif symbol == pyglet.window.key.DOWN:
            self.pacman.move(0,-60)

if __name__ == "__main__":
    sys.setrecursionlimit(1500)
    cocos.director.director.init(width=540,height=540)
    game = PacmanGame()
    main_stage = cocos.scene.Scene (game)
    cocos.director.director.run (main_stage)
