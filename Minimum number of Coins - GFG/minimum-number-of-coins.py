#User function Template for python3

class Solution:
    def minPartition(self, N):
        ans=[]
        if N>=2000:
            x=N//2000
            N=N%2000
            for i in range(x):
                ans.append(2000)
        if N>=500:
            x=N//500
            N=N%500
            for i in range(x):
                ans.append(500)
        if N>=200:
            x=N//200
            N=N%200
            for i in range(x):
                ans.append(200)
        if N>=100:
            x=N//100
            N=N%100
            for i in range(x):
                ans.append(100)
        if N>=50:
            x=N//50
            N=N%50
            for i in range(x):
                ans.append(50)
        if N>=20:
            x=N//20
            N=N%20
            for i in range(x):
                ans.append(20)
        if N>=10:
            x=N//10
            N=N%10
            for i in range(x):
                ans.append(10)
        if N>=5:
            x=N//5
            N=N%5
            for i in range(x):
                ans.append(5)
        if N>=2:
            x=N//2
            N=N%2
            for i in range(x):
                ans.append(2)
        if N>=1:
            x=N//1
            N=N%1
            for i in range(x):
                ans.append(1)
        return ans
        
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        arr = ob.minPartition(N)
        for i in range(len(arr)):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends