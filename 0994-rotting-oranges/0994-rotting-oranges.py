class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        d = {0:0, 1:0, 2:0} #create a hashtable for 0,1,2 
        time = -1
        idx_rot = []
		
		#find index of 2
        for i,row in enumerate(grid):
            for j,col in enumerate(row):
                d[col] += 1
                if col==2:
                    idx_rot.append((i, j))
        if d[1] == 0:
            return 0
        while idx_rot: 
            temp = []
            #each iteration will have indices of twos that got converted in last iteration
            for i,j in idx_rot:
                #iterate 4-directionally 
                for m,n in [(i-1,j), (i+1, j), (i, j-1), (i, j+1)]:
        
                    if m<0 or m>=len(grid) or n<0 or n>=len(grid[0]):
                        continue
                    elif grid[m][n] == 1:
        
                        grid[m][n] = 2
                        d[1] -= 1  #reduce count of 1's (incase an orange is isolated we will have non-zero count for 1
                        temp.append((m,n))  
                    
            #update idx_rot (index of rotten oraange) with temp
            idx_rot = temp
            time += 1  #increment time
		#check for non-zero count of 1s
        if d[1] != 0:
            return -1
        return time