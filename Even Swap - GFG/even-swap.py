#User function Template for python3

class Solution():
    def lexicographicallyLargest(self, a, n):
        #your code here
        temp=[];c=2;res=[]
        for i in range(n):
            if a[i]%2==0:
                if c==0:
                    temp.sort(reverse=True)
                    res+=temp
                    temp=[]
                c=1
                temp.append(a[i])
            else:
                if c==1:
                    temp.sort(reverse=True)
                    res+=temp
                    temp=[]
                c=0
                temp.append(a[i])
        temp.sort(reverse=True)
        res+=temp
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        a = [int(i) for i in input().split()]
        ans = Solution().lexicographicallyLargest(a, n)
        for i in ans:
            print(i,end=" ")
        print()

# } Driver Code Ends