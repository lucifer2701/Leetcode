from collections import Counter
class Solution:
    def maxInstance(self, s : str) -> int:
        # code here
        c=Counter(s)
        x=['b','a','l','o','n'];ans=float('inf')
        for i in x:
            if i not in c:
                return 0
            if i=='l' or i=='o':
                ans=min(c[i]//2,ans)
            else:
                ans=min(c[i],ans)
        return ans
                


#{ 
 # Driver Code Starts
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        s = (input())
        
        obj = Solution()
        res = obj.maxInstance(s)
        
        print(res)

# } Driver Code Ends