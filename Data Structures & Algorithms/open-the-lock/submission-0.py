class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        
        deadendSet = set([tuple(map(int, "".join(deadend))) for deadend in deadends])
        targetTup = tuple(map(int, "".join(target)))
        print(targetTup)
        print(deadendSet)

        visited = set()


        q = deque()

        q.append([0,0,0,0])

        MOD = 10
        res = -1


        while q:
            qlen = len(q)
            res += 1

            for _ in range(qlen):
                combination = q.popleft() # (a,b,c,d)
                #print(combination, res)

                if tuple(combination) in deadendSet:
                    continue

                if tuple(combination) in visited:
                    continue

                if tuple(combination) == targetTup:
                    return res

                visited.add(tuple(combination))
                for i in range(4):
                    newCombination = combination.copy()
                    newCombination[i] = (newCombination[i] + 1) % MOD
                    q.append(newCombination)

                    newCombination = combination.copy()
                    newCombination[i] = (newCombination[i] - 1) % MOD
                    q.append(newCombination)

        return -1