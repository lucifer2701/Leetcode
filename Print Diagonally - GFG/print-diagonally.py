#User function Template for python3

def downwardDigonal(n, A): 
    c = []
    for l in range(2*n-1):
        t, b = max(0, l+1-n), min(l, n-1)
        for i in range(t, b+1):
            c.append(A[i][l-i])
    return c


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        matrix =[]
        for i in range(n):
            row = list(map(int, input().strip().split()))
            matrix.append(row)
        ans = downwardDigonal(n,matrix)
        for i in ans:
            print(i,end=" ")
        print()

# } Driver Code Ends