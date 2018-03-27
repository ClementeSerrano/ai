import cocos
import pyglet
import random
import sys
import math
from laberinto import *
from pacman import *
from fantasma import *
from comida import *

class JuegoPacman(cocos.layer.Layer):
    is_event_handler=True

    def __init__(self):
        super(JuegoPacman, self ).__init__()
        self.laberinto=Laberinto()

        self.pacman=Pacman(self.laberinto)
        x,y=self.laberinto.posicion_centro_celda(5,4)
        self.pacman.sprite.x=x
        self.pacman.sprite.y=y

        self.atlas_items=pyglet.image.load("resources/comida.png")
        self.imagen_item=pyglet.image.ImageGrid(self.atlas_items,1,16)

        self.fantasma1=Fantasma(self.laberinto)
        x,y=self.laberinto.posicion_centro_celda(3,4)
        self.fantasma1.sprite.x=x
        self.fantasma1.sprite.y=y

        self.comida0=Comida(0,False,10,self.imagen_item[0])
        self.laberinto.posicionar(8,0,self.comida0)

        self.comida1=Comida(1,False,20,self.imagen_item[1])
        self.laberinto.posicionar(0,8,self.comida1)

        self.puntaje=0
        self.etiqueta_marcador=cocos.text.Label("Score:",(190,450),font_size=16,bold=True)
        self.marcador=cocos.text.Label(str(self.puntaje).zfill(2),(270,450),font_size=16,bold=True)

        self.add(self.laberinto.sprite,z=0)
        self.add(self.pacman.sprite,z=1)
        self.add(self.fantasma1.sprite,z=1)
        self.add(self.comida0.sprite,z=1)
        self.add(self.comida1.sprite,z=1)
        self.add(self.etiqueta_marcador,z=1)
        self.add(self.marcador,z=1)
        self.schedule_interval(self.simular,0.5)

    def simular(self,*args,**kwargs):
        self.marcador.element.text=str(self.pacman.puntaje).zfill(2)
        self.fantasma1.animar(self.pacman.sprite.x,self.pacman.sprite.y)

    def on_key_press(self, symbol, modifiers):
        if symbol == pyglet.window.key.RIGHT:
            self.pacman.mover(60,0)
        elif symbol == pyglet.window.key.LEFT:
            self.pacman.mover(-60,0)
        elif symbol == pyglet.window.key.UP:
            self.pacman.mover(0,60)
        elif symbol == pyglet.window.key.DOWN:
            self.pacman.mover(0,-60)

if __name__ == "__main__":
    sys.setrecursionlimit(1500)
    cocos.director.director.init(width=540,height=540)
    juego = JuegoPacman()
    escena_principal = cocos.scene.Scene (juego)
    cocos.director.director.run (escena_principal)
