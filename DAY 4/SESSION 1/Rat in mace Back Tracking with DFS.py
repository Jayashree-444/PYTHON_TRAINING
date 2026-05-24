class BikeThePath:
    N=4
    
    def findPath(self,maze,row,col,sol):
        if row==self.N-1 and col==self.N-1:
            print(path)
            return True
        if maze[row][col]==1:
            return False
        if maze[row][col]==0 and row==self.N and col==self.N:
            return False
            
            maze[row][col]=0
            
            if self.findPath(maze,row+1,col,path+"D"):
                return True
            
            maze[row][col]=1 # 1 is revisited
            
             

#main
maze=[[1, 0, 0, 0], [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1]]
    obj=BikeAndThePath()
    obj


for i in range(4):
    row=list(map(int,input().split()));
        maze.append(row);
    