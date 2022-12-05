#User function Template for python3

class Solution:
    def longestCommonPrefix(self, arr, n):
        arr.sort(key=len)
        temp=arr[0];li=[]
        for i in arr:
            t=''
            for j in range(len(temp)):
                if temp[j]==i[j]:
                    t+=temp[j]
                else:
                    break
            li.append(t)
        li.sort(key=len)
        if len(li[0])==0:
            return -1
        return li[0]
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n = int(input())
        arr = [x for x in input().strip().split(" ")]
        
        ob=Solution()
        print(ob.longestCommonPrefix(arr, n))
# } Driver Code Ends