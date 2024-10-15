# Дан бинарный сетка размером m x n, где каждая 1 обозначает дом одного друга. Верните минимальное общее расстояние путешествия.
# Общее расстояние путешествия — это сумма расстояний между домами друзей и точкой встречи.
# Расстояние рассчитывается по Манхэттенскому расстоянию, где distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.

"""
Input: grid = [[1,0,0,0,1],[0,0,0,0,0],[0,0,1,0,0]]
Output: 6
"""

class Solution:
    def minTotalDistance(self, grid: list[list[int]]) -> int:
        minDistance = float('inf')
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                distance = self.search(grid, row, col)
                minDistance = min(distance, minDistance)
        return minDistance

    def search(self, grid: list[list[int]], row: int, col: int) -> int:
        q = [(row, col, 0)]
        m = len(grid)
        n = len(grid[0])
        visited = [[False] * n for _ in range(m)]
        totalDistance = 0
        
        while q:
            r, c, d = q.pop(0)
            
            if r < 0 or c < 0 or r >= m or c >= n or visited[r][c]:
                continue
            
            if grid[r][c] == 1:
                totalDistance += d
            
            visited[r][c] = True
            
            q.append((r + 1, c, d + 1))
            q.append((r - 1, c, d + 1))
            q.append((r, c + 1, d + 1))
            q.append((r, c - 1, d + 1))
        
        return totalDistance
    
if __name__ == "__main__":
    example = Solution()
    res = example.minTotalDistance(grid = [[1,0,0,0,1],[0,0,0,0,0],[0,0,1,0,0]])
    print(res)