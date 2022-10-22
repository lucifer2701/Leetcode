#User function Template for python3
class Solution:
	def reverseSpiral(self, R, C, a):
		# code here
		t=n=R*C
		r,c=0,0
		rn,cn=R,C
		li=[];ans=[]
		if rn==1:
		    ans=a[0]
		    ans.reverse()
		    return ans
		if cn==1:
		    for i in range(rn):
		        ans.append(a[i][0])
		    ans.reverse()
		    return ans
		while t!=0:
		    for i in range(c,cn):
		        li.append(a[r][i])
		        t-=1
		    if t==0:    break
		    r+=1
		    for i in range(r,rn):
		        li.append(a[i][cn-1])
		        t-=1
		    if t==0:    break
		    cn-=1
		    for i in range(cn-1,c-1,-1):
		        li.append(a[rn-1][i])
		        t-=1
		    if t==0:    break
		    rn-=1
		    for i in range(rn-1,r-1,-1):
		        li.append(a[i][c])
		        t-=1
		    if t==0:    break
		    c+=1
		ans=li[:n]
		ans.reverse()
        return ans



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        R,C=[int(x) for x in input().split()]
        a=[[0]*C for c in range(R)]
        arr=input().split()
        for i in range(R*C):
            a[i//C][i%C]=int(arr[i])
            
        ob=Solution()
        ans=ob.reverseSpiral(R,C,a)
        for i in range(len(ans)):
            print(ans[i],end=" ")
            
        print()
# } Driver Code Ends