class TrieNode:
   def __init__(self,char):
       self.char=char
       self.children={}
class Solution:
   def insert(node,word):
       head=node
       for c in word:
           if c not in head.children.keys():
               new_node=TrieNode(c)
               head.children[c]=new_node
               head=new_node
           else:
               head=head.children[c]
       head.isEnd=True
   def query(node,word):
       head=node
       c,prefix=0,""
       sen=""
       while c<len(word):
           tmp=False
           sen+=word[c]
           if len(head.children)>1:
               tmp=True
               prefix=sen
           head=head.children[word[c]]
           c+=1
       if prefix=="":
           prefix=sen
       return prefix
   def findPrefixes(self, arr, N):
       root=TrieNode('-1')
       out=[]
       for string in arr:
           Solution.insert(root,string)
       for string in arr:
           out.append(Solution.query(root,string))
       return out


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        arr=list(map(str,input().split()))
        
        ob = Solution()
        res = ob.findPrefixes(arr,N)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends