class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid:
            return 0

        ROWS, COLS = len(grid), len(grid[0])

        def bfs(r,c):
            
            q = collections.deque()
            q.append((r,c))
            direc = [[1,0],[-1,0],[0, -1], [0,1]]

            while q:
            
                qlen = len(q)
                r, c = q.popleft()
                for dr, dc in direc:
                    nr, nc = r + dr, c + dc
                    if (
                        0 <= nr < ROWS and
                        0 <= nc < COLS and
                        grid[nr][nc] == "1"
                    ):
                        grid[nr][nc] = "0"
                        q.append((nr, nc))


        res = 0

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1":
                    bfs(i, j)
                    res += 1
        return res