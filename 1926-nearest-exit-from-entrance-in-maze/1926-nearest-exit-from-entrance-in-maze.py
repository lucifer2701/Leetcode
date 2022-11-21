class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        row,column=len(maze),len(maze[0])
        entrance_row,entrance_column=entrance[0],entrance[1]
        points=[(1,0),(-1,0),(0,1),(0,-1)]
        q=collections.deque([[entrance_row,entrance_column,0]])
        maze[entrance_row][entrance_column]="+"
        while q:
            current_row,current_column,steps=q.popleft()
            for x,y in points:
                new_row=current_row+x
                new_column=current_column+y
                if 0<= new_row < row and 0<= new_column < column and maze[new_row][new_column]==".":
                    if new_row==0 or new_row==row-1 or new_column==0 or new_column==column-1:
                        return steps+1
                    maze[new_row][new_column]="+"
                    q.append([new_row,new_column,steps+1])
                    
        
        return -1