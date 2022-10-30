class Solution:
    # bfs
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        # y, x, remain, steps
        queue = collections.deque([(0, 0, k, 0)])
        visited = set()
        
        while queue:
            for i in range(len(queue)):
                y, x, remain, steps = queue.popleft()
                if y == m-1 and x == n-1: return steps            
                UDLR = [(y-1, x), (y+1, x), (y, x-1), (y, x+1)]
                for yy, xx in UDLR:
                    if 0 <= yy < m and 0 <= xx < n \
                       and (yy, xx, remain) not in visited:
                        visited.add((yy, xx, remain))
                        if grid[yy][xx] == 0:
                            queue.append((yy, xx, remain, steps+1))
                        elif remain > 0:
                            queue.append((yy, xx, remain-1, steps+1))
        return -1