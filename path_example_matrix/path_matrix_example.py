#Resolution, path and movements of ghost
#in PACMAN GAME between to points

N = 9 #size of matrix
#board of the game in a matrix of 9x9
board_game = [
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



#Matrix with coord_path
solution_path = [[0]*N for _ in range(N)]
coord_path=[]


#BACKTRACKING
def resolve_path(r, c,x_end,y_end):
    x_end+=1
    y_end+=1
   
    #If we get the result the function ends
    #the target is x_end,y_end that represent the obj
    if (r==x_end-1) and (c==y_end-1):
        solution_path[r][c] = 1;
        coord_path.append((r,c))
        print("Ini : 3 , 4 \n")
        print("Obj :",r,",",c)
        return True;
    #check if safe to visit the cells in IF 
    if r>=0 and c>=0 and r<x_end and c<y_end and solution_path[r][c] == 0 and board_game[r][c] == 0:
        #if safe to visit then visit the cell
        solution_path[r][c] = 1
        #down
        if resolve_path(r+1, c,x_end-1,y_end-1):
            coord_path.append((r,c))
            return True
        #rigth
        if resolve_path(r, c+1,x_end-1,y_end-1):
            coord_path.append((r,c))
            return True
        #up
        if resolve_path(r-1, c,x_end-1,y_end-1):
            coord_path.append((r,c))
            return True
        #left
        if resolve_path(r, c-1,x_end-1,y_end-1):
            coord_path.append((r,c))
            return True
        #if not posible make a move then the cell is 0
        #and return False
        solution_path[r][c] = 0;
        return False;
    
    return 0;

#print the matrix to see the walls and
#the spaces of the game in this case
#the spaces is      " . "
#and the walls are  " # "
print("BOARD GAME\n")
for i in range(len(board_game)):
    for j in range(len(board_game[i])):
        if(board_game[i][j]==0):
            print(".",end=" ")
        else:
            print("#",end=" ")
    print(" ")

print(" ")
print("\nPATH SOLUTION\n")
#resolve_path recive the coord Ini: 2,4
#and de the obj the in this case is 5,5
if(resolve_path(2,4,5,5)):
    
    coord_path.reverse()
    print("\nCOORD OF THE PATH : ",coord_path)
    for i in range(len(coord_path)):
        for j in range(2):
            if(j==0):
                row=coord_path[i][j]
            else:
                col=coord_path[i][j]
        
        board_game[row][col]=-1
    print("\n")
    for i in range(len(board_game)):
        for j in range(len(board_game[i])):
            if(board_game[i][j]==-1 ):
                    
                print("O",end=" ")
            if(board_game[i][j]==1):
                print("#",end=" ")
            if(board_game[i][j]==0):
                print(".",end=" ")
            
        print(" ")
    
    
else:
    print ("No solution")


