class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''

                1,           5,           10
                /|\\          /|\\          /|\\
            2 6 11.     6 10 X15.    11 X X
                            /|\\


            using bfs the first encounter with amount  will be the at the breath count equal to results

            we will use a visted set to stop repeat work

            base case: 
            - value in visited
            - value exceeds amount

        '''

        if amount == 0:
            return 0

        visited = set()

        q = deque()
        for coin in coins:
            q.append(coin)
        
        res = 0
        while q:
            res += 1

            lenQ = len(q)
            for _ in range(lenQ):
                total = q.popleft()
                if total in visited:
                    continue
                if total > amount:
                    continue
                if total == amount:
                    return res

                visited.add(total)
                for coin in coins:
                    
                    if total + coin not in visited:
                        total += coin 
                        q.append(total)
                        total -= coin 
        
        return -1









