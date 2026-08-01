class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        

        maxA = 0

        ROWS = len(grid)
        COLS = len(grid[0])

        def bfs(r, c):
            area = 1
            
            q = collections.deque()
            direc = [[1,0],[-1,0],[0, -1], [0,1]]
            q.append((r,c))
            grid[r][c] = 0 

            while q:
                r, c = q.popleft()

                for dr, dc in direc:
                    nr, nc = r + dr, c + dc

                    if (0 <= nr < ROWS and
                    0 <= nc < COLS and
                    grid[nr][nc] == 1):
                        area += 1
                        print(area)
                        grid[nr][nc] = 0
                        q.append((nr, nc)) 
            return area


        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    maxA = max(maxA, bfs(i, j))
        return maxA



