
class Solution:
    def characterReplacement(self, s, k):
        i=j=maxlen=ans=0
        Map={}
        while j<len(s):
            if s[j] in Map:
                Map[s[j]]+=1
            else:
                Map[s[j]]=1
            
            maxlen=max(maxlen,Map[s[j]])
            if ((j-i+1)-maxlen>k):
                Map[s[i]]-=1
                i+=1
            ans=max(ans,j-i+1)
            j+=1
        return ans
        
        
            
            



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		k = int(input())
		ob = Solution()
		ans = ob.characterReplacement(s, k)
		print(ans)

# } Driver Code Ends