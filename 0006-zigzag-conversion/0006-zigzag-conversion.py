class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows == 1: return s
        arr = [[] for i in range(numRows)]
        row = 0
        direction = 'down'
        
        for c in s:
            arr[row].append(c)
            row = row + 1 if direction == 'down' else row - 1
            if row == 0: direction = 'down'
            if row == numRows-1: direction = 'up'
            
        return ''.join([''.join(row) for row in arr])