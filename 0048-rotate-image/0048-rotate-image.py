class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix[:]=list(zip(*reversed(matrix)))