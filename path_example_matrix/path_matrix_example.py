
'''
N = 9
#maze problem
laberinto = [
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
#MAZE
print("MATRIZ INICIAL\n")
for i in range(len(laberinto)):
    for j in range(len(laberinto[i])):
        if(laberinto[i][j]==0):
            print(".",end=" ")
        else:
            print("#",end=" ")
    print(" ")

print(" ")
#se llena la lista de ceros
solucion = [[0]*N for _ in range(N)]
coordenadas=[]


#BACKTRACKING
def resolverpath(r, c,x_fin,y_fin):
    x_fin+=1
    y_fin+=1
   
    #Si se llega al resultado, se termina la funcion
    #se toma en consideracion x_fin,y_fin como coordenadas target
    if (r==x_fin-1) and (c==y_fin-1):
        solucion[r][c] = 1;
        coordenadas.append((r,c))
        print("Se llego al punto objetivo R",r,"C",c)
        return True;
    #se chequea si es posible acceder a una celda
    #solution[r][c] == 0 se ve si no se ha visitado
    #maze[r][c] == 0 se ve si no esta bloqueado
    if r>=0 and c>=0 and r<x_fin and c<y_fin and solucion[r][c] == 0 and laberinto[r][c] == 0:
        #if safe to visit then visit the cell
        solucion[r][c] = 1
        #hacia abajo
        if resolverpath(r+1, c,x_fin-1,y_fin-1):
            coordenadas.append((r,c))
            return True
        #hacia la derecha
        if resolverpath(r, c+1,x_fin-1,y_fin-1):
            coordenadas.append((r,c))
            return True
        #hacia arriba
        if resolverpath(r-1, c,x_fin-1,y_fin-1):
            coordenadas.append((r,c))
            return True
        #hacia la izquierda
        if resolverpath(r, c-1,x_fin-1,y_fin-1):
            coordenadas.append((r,c))
            return True
        #backtracking
        solucion[r][c] = 0;
        return False;
    
    return 0;
if(resolverpath(2,4,4,8)):
    print("\nPATH RESULTANTE \n")
    for i in range(len(solucion)):
        for j in range(len(solucion[i])):
            if(solucion[i][j]==1):
                print("*",end=" ")
            else:
                print(".",end=" ")
            
        print(" ")
    coordenadas.reverse()
    print("coordenadas",coordenadas)
else:
    print ("No solution")

'''
def solveMaze( Maze , position , x_fin, y_fin ):
    # returns a list of the paths taken
    if position == ( x_fin, y_fin  ):
        return [ ( x_fin, y_fin ) ]
    x , y = position
    if x + 1 < x_fin and Maze[x+1][y] == 1:
        a = solveMaze( Maze , ( x + 1 , y ) , x_fin, y_fin )
        if a != None:
            return [ (x , y ) ] + a

    if y + 1 < y_fin and Maze[x][y+1] == 1:
        b = solveMaze( Maze , (x , y + 1) , x_fin, y_fin )
        if  b != None:
            return [ ( x , y ) ] + b


Maze = [[ 1 , 0 , 1, 0 , 0],
        [ 1 , 1 , 0, 1 , 0],
        [ 0 , 1 , 0, 1 , 0],
        [ 0 , 1 , 0, 0 , 0],
        [ 1 , 1 , 1, 1 , 1]
        ]

print(solveMaze(Maze,(0,0),2,1))



