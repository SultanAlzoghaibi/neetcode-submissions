class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        res = 0
        DIRECTION = [(1,0), (0,1)]

        cache = defaultdict(int)
        def dfs(r,c):

            if r == m-1 and c == n -1:
                cache[(r,c)] = 1
                return 1 

            if (r,c) in cache:
                cache[(r,c)] 
                return cache[(r,c)]

            total = 0
            for moveR, moveC in DIRECTION:
                
                newR = moveR + r
                newC = moveC + c

                if 0 <= newR < m and 0 <= newC < n:
                    total += dfs(newR, newC)
            cache[(r,c)] = total
            return total

        return dfs(0,0)

            
            
            

        
        