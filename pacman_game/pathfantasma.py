

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
    #print("X inicial",r,"Y inicial",c)
   
    #Si se llega al resultado, se termina la funcion
    #se toma en consideracion x_fin,y_fin como coordenadas target
    if (r==x_fin-1) and (c==y_fin-1):
        solucion[r][c] = 1;
        coordenadas.append((r,c))
        print("OBJ: ",r,",",c)
        
        return True;
    #se chequea si es posible acceder a una celda
    #solution[r][c] == 0 se ve si no se ha visitado
    #maze[r][c] == 0 se ve si no esta bloqueado
    if r>=0 and c>=0 and r<N and c<N and solucion[r][c] == 0 and laberinto[r][c] == 0:
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
    #print("objetivo X",x_fin-1,"Y",y_fin-1)
    return 0;






