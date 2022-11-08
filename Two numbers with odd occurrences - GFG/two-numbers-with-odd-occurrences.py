from collections import Counter
#User function Template for python3
class Solution:
    def twoOddNum(self, Arr, N):
        ans=[]
        d=Counter(Arr)
        for ele in d :
            if d[ele]%2==1:
                ans.append(ele)
        a=max(ans[0],ans[1])
        b=min(ans[0],ans[1])
        return [a,b]



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        N = int(input())
        Arr = input().split()
        for itr in range(N):
            Arr[itr] = int(Arr[itr])
        ob = Solution();
        ans = ob.twoOddNum(Arr,N)
        for i in range(len(ans)):
        	print(ans[i], end = " ")
        print()
# } Driver Code Ends