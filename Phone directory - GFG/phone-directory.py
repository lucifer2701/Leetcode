#User function Template for python3
class Solution:
    def displayContacts(self, n, contact, s):
        # code here
        contact=set(contact)
        contact=list(contact)
        finalans=[]
        for i in range(len(s)):
            x=s[:i+1]
            ans=[]
            for ele in contact:
                if x==ele[:len(x)]:
                    ans.append(ele)
            ans.sort()
            if len(ans)==0: ans.append(0)
            finalans.append(ans)
        return finalans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        contact = input().split()
        s = input()
        
        ob = Solution()
        ans = ob.displayContacts(n, contact, s)
        for i in range(len(s)):
            for val in ans[i]:
                print(val, end = " ")
            print()
# } Driver Code Ends