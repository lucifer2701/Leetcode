#User function Template for python3
import sys
class Solution:
    def travel(inx,visited,dp,cost,v):
        if visited>v:
            return 0
        if visited==v:
            return cost[inx][0]
        ans=sys.maxsize
        for j in range(1,v):
            if inx!=j and dp[j]==-1:
                dp[j]=1
                visited+=1
                ans=min(ans,cost[inx][j]+Solution.travel(j,visited,dp,cost,v))
                dp[j]=-1
                visited-=1
        return ans
    def total_cost(self, cost):
        if len(cost)==1:
            return cost[0][0]
        dp=[-1 for i in range(len(cost)+1)]
        dp[0]=-1
        return Solution.travel(0,1,dp,cost,len(cost))

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		cost = []
		for _ in range(n):
			cost.append(list(map(int, input().split())))
		obj = Solution()
		ans = obj.total_cost(cost)
		print(ans)

# } Driver Code Ends