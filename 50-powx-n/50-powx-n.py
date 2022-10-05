class Solution:
    def myPow(self, x: float, n: int) -> float:
        #O(logn) Time and O(1) space
        if n<0:
            x=1/x
            n=-n
        
        ans,curr=1,x
        
        i=n
        while i:
            if i%2 ==1:
                ans =ans * curr
            curr=curr*curr
            i=i//2
        return ans