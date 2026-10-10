class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        '''
        
        sides = [0,0,0,0]
        [1,0,0,0]
        [0,0,0,1]
        we cache by a tuple where the sorted sides Arr can tells us a bool

        cahce = {}

        A) we reach the end of arr
        B) A cache is hit
        C) return flag ture


        '''
        cache = {}
        total = sum(matchsticks)
        if total % 4:
            return False

      
        foundSquare = False
        def dfs(sides: list[int], i):
            nonlocal foundSquare
            #print(sides, i)

            if i == len(matchsticks):
                if len(set(sides)) == 1:
                    foundSquare = True
                    return True
                return False

            if foundSquare:
                return True
       
            if tuple(sorted(sides)) in cache:
                return cache[tuple(sorted(sides))]
            
            isSquare = False

            for j in range(4):
                sides[j] += matchsticks[i]
                isSquare = isSquare or dfs(sides, i+1)
                sides[j] -= matchsticks[i]

            
            cache[tuple(sorted(sides))] = isSquare
            return isSquare
        

        return dfs([0,0,0,0], 0)