#User function Template for python3
from collections import Counter
class Solution:
    
    #Function to remove pair of duplicates from given string using Stack.
    def removePair(self,s):
        # code here
        d=[""]
        for i in s:
            if d[-1]==i:
                d.pop()
            else:
                d.append(i)
        if len(d)>1:
            return "".join(d)
        return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

#Contributed by : Nagendra Jha


_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())
    


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        obj = Solution()
        print(obj.removePair(str(input())))
# } Driver Code Ends