#User function Temp
from collections import deque 
class Solution:
 def left(self,arr,n):
   # search for the nearest smaller height on left side .. 
   result = [-1]*n
   stack = deque()
   stack.append(0)
   for i in range(1,n):
     currH = arr[i] 
     if stack and arr[stack[-1]]<currH:
       result[i] = stack[-1] 
     else:
       while stack and arr[stack[-1]]>=currH:
         stack.pop() 
       if stack:
         result[i] = stack[-1] 
     stack.append(i)
   return result
   
 def right(self,arr,n):
   # search for the nearest smaller on the right side..to get width..
   stack = deque()
   stack.append(n-1)
   result=[n]*n 
   for i in range(n-2,-1,-1):
     currH = arr[i]
     if stack and arr[stack[-1]]<currH:
       result[i] = stack[-1] 
     else:
       while stack and arr[stack[-1]]>=currH:
         stack.pop() 
       
       if stack:
         result[i] = stack[-1]
     stack.append(i)
   return result 
   
 def getMaxArea(self,arr,n):
   left = self.left(arr,n)
   right = self.right(arr,n)
   _maxArea = 0 
   for i in range(n):
     currArea = ((right[i]-left[i])-1)*(arr[i])
     _maxArea = max(_maxArea,currArea)
   return _maxArea
 
 def maxArea(self,matrix,n,m):
   maxArea = 0 
   height=[0]*m 
   for i in range(n):
   
     for j in range(m):
       if matrix[i][j] == 0:
         height[j] = 0 
       else:
         height[j]+=matrix[i][j]
     maxArea = max(maxArea, self.getMaxArea(height,m))
   return maxArea


#{ 
 # Driver Code Starts
#Initial Template for Python 3



# Driver Code 
if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        R,C = map(int, input().strip().split())
        A = []
        for i in range(R):
            line = [int(x) for x in input().strip().split()]
            A.append(line)
        print(Solution().maxArea(A, R, C)) 
	
# This code is contributed 
# by SHUBHAMSINGH10 

# } Driver Code Ends