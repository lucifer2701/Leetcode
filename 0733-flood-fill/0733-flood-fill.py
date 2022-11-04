class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        
        queue = [(sr, sc)]
        visited = set()
        val = image[sr][sc]
        
        if val == color:
            return image
        
        # maintain a list of flood points to fill
        flood = [(sr, sc)]

        while queue:
            cell = queue.pop(0)
            visited.add(cell)
            neighbors = [(0,1), (0,-1), (1, 0), (-1,0)]
            
            for newcell in neighbors:
                ele = (cell[0] + newcell[0], cell[1] + newcell[1])
                if 0 <= ele[0] < m and 0 <= ele[1] < n and ele not in visited and image[ele[0]][ele[1]] == val:
                    flood.append(ele)
                    queue.append(ele)
                    visited.add(ele)
        
        for pt in flood:
            image[pt[0]][pt[1]] = color
        
        return image