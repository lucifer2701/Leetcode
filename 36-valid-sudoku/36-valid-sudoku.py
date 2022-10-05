class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ans=0
        for i in range(9):
            l=[]
            for j in range(9):
                l.append(board[i][j])
            x = max(set(l), key=l.count)
            p=l.count(x)
            for k in range(p):
                l.remove(x)
            if len(l)!=0 :
                x = max(set(l), key=l.count)
                p=l.count(x)
            else: 
                p=0
            if (p>1):
                ans=0
            else:
                ans+=1
        for i in range(9):
            m = []
            for j in range(9):
                m.append(board[j][i])
            x = max(set(m), key=m.count)
            p = m.count(x)
            for k in range(p):
                m.remove(x)
            if len(m)!=0 :
                x = max(set(m), key=m.count)
                p = m.count(x)
            else: 
                p=0
            if (p > 1):
                ans = 0
            else:
                ans += 1
        y=0
        for j in range(3):
            l = []
            for k in range(y, y + 3):
                for m in range(3):
                    l.append(board[k][m])

            y += 3
            x = (max(set(l), key=l.count))
            p = l.count(x)
            for k in range(p):
                l.remove(x)
            if len(l) != 0:
                x = max(set(l), key=l.count)
                p = l.count(x)
            else:
                p = 0
            if (p > 1):
                ans = 0
            else:
                ans += 1
        y = 0
        for j in range(3):
            l = []
            for k in range(y, y + 3):
                for m in range(3, 6):
                    l.append(board[k][m])
            y += 3
            x = (max(set(l), key=l.count))
            p = l.count(x)
            for k in range(p):
                l.remove(x)
            if len(l) != 0:
                x = max(set(l), key=l.count)
                p = l.count(x)
            else:
                p = 0
            if (p > 1):
                ans = 0
            else:
                ans += 1
        y = 0
        for j in range(3):
            l = []
            for k in range(y, y + 3):
                for m in range(6, 9):
                    l.append(board[k][m])
            y += 3
            x =(max(set(l), key=l.count))
            p = l.count(x)
            for k in range(p):
                l.remove(x)
            if len(l) != 0:
                x = max(set(l), key=l.count)
                p = l.count(x)
            else:
                p = 0
            if (p > 1):
                ans = 0
            else:
                ans += 1
        if ans==27:
            return 1
        else:
            return 0