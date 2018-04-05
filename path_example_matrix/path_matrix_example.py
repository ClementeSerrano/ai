# Author: Christian Careaga (christian.careaga7@gmail.com)
# A* Pathfinding in Python (2.7)
# Please give credit if used

import numpy
from heapq import *

nmap = numpy.array([
            [0,0,0,0,0,0,0,0,0],
            [0,1,0,1,1,1,0,1,0],
            [0,0,0,0,0,0,0,0,0],
            [1,1,0,1,0,1,0,1,1],
            [0,1,0,1,1,1,0,1,0],
            [0,1,0,0,0,0,0,1,0],
            [0,0,0,1,1,1,0,0,0],
            [0,1,0,1,0,1,0,1,0],
            [0,0,0,0,0,0,0,0,0]])

solucionpath =[
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0]]

def heuristic(a, b):
    return (b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2

def astar(start, goal):

    neighbors = [(0,1),(0,-1),(1,0),(-1,0)]

    close_set = set()
    came_from = {}
    gscore = {start:0}
    fscore = {start:heuristic(start, goal)}
    oheap = []

    heappush(oheap, (fscore[start], start))
    
    while oheap:

        current = heappop(oheap)[1]

        if current == goal:
            data = []
            while current in came_from:
                data.append(current)
                current = came_from[current]
            return data

        close_set.add(current)
        for i, j in neighbors:
            neighbor = current[0] + i, current[1] + j            
            tentative_g_score = gscore[current] + heuristic(current, neighbor)
            if 0 <= neighbor[0] < nmap.shape[0]:
                if 0 <= neighbor[1] < nmap.shape[1]:                
                    if nmap[neighbor[0]][neighbor[1]] == 1:
                        continue
                else:
                    # array bound y walls
                    continue
            else:
                # array bound x walls
                continue
                
            if neighbor in close_set and tentative_g_score >= gscore.get(neighbor, 0):
                continue
                
            if  tentative_g_score < gscore.get(neighbor, 0) or neighbor not in [i[1]for i in oheap]:
                came_from[neighbor] = current
                gscore[neighbor] = tentative_g_score
                fscore[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                
                heappush(oheap, (fscore[neighbor], neighbor))
                
    return False

'''Here is an example of using my algo with a numpy array,
   astar(array, start, destination)
   astar function returns a list of points (shortest path)'''




print("Pacman 0 , 0")
print("Fantasma  8 , 8")
arreglo=[] 
inicial=[(8,8)]
arreglo+=astar((8,8), (0,0))
arreglo.reverse()
movimiento=[(0,1),(0,-1),(1,0),(-1,0)]
print("\nPath Encontrado",arreglo)

for a in range(len(arreglo)):
    l=[]
    for i in range(2):
        if(i==0):
            row=arreglo[a][i]
            
        else:
            col=arreglo[a][i]
    l.append((row,col))   
    #print("LLL",l[0])    
    
    #arriba 
    if((tuple(map(sum, zip(inicial[0], movimiento[0]))))==l[0]):
        print("derecha")
    #abajo
    if((tuple(map(sum, zip(inicial[0], movimiento[1]))))==l[0]):
        print("izquierda")
    #derecha
    if((tuple(map(sum, zip(inicial[0], movimiento[2]))))==l[0]):
        print("abajo")
    #izquierda
    if((tuple(map(sum, zip(inicial[0], movimiento[3]))))==l[0]):
        print("arriba")
    inicial=[]
    inicial.append(arreglo[a])
for a in range(len(arreglo)):
    for i in range(2):
        if(i==0):
            row=arreglo[a][i]
            
        else:
            col=arreglo[a][i]
    solucionpath[row][col]=1

print("\nSOLUCION EN MATRIZ ")
#se agrega un -1 para la posicion del fantasma
solucionpath[8][8]=-1
for a in range(len(solucionpath)):
    for b in range(len(solucionpath[a])):
        if(solucionpath[a][b]==0):
            print(".",end=" ")
        elif(solucionpath[a][b]==-1):
            print("*",end=" ")
        else:
            print("o",end=" ")
    print(" ")

