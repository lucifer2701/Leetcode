class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        seen = {0}
        stack = [0]
        
        while stack:
            vertex = stack.pop()
            for neighbor in rooms[vertex]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    stack.append(neighbor)
                    
        return len(seen) == len(rooms)