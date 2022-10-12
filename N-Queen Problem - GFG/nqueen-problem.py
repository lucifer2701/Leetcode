class Solution:

    def nQueen(self, n):

        # code here

        col=set()

        neg=set()

        pos=set()

        board=[["."]*n for i in range(n)]

        res=[]

        

        def back(r):

            if(r==n):

                res.append([row.index("Q")+1 for row in board])

                return

            for c in range(n):

                if(c in col or (r+c) in pos or (r-c) in neg):

                    continue

                col.add(c)

                neg.add(r-c)

                pos.add(r+c)

                board[r][c]="Q"

                back(r+1)

                col.remove(c)

                pos.remove(r+c)

                neg.remove(r-c)

                board[r][c]="."

        back(0)

        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        ob = Solution()
        ans = ob.nQueen(n)
        if(len(ans) == 0):
            print("-1")
        else:
            for i in range(len(ans)):
                print("[",end="")
                for j in range(len(ans[i])):
                    print(ans[i][j],end = " ")
                print("]",end = " ")
            print()
                
# } Driver Code Ends