class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        '''
            


            [0,1]

            using vistised we can stop a bfs call from looping back 

        '''


        adjMap = defaultdict(list)


        for start, end in edges:
            adjMap[start].append(end)
            adjMap[end].append(start)


        print(adjMap)
        
        heights = []
        

        for root in range(n):

            q = deque()
            visited = set()
            q.append(root)
            height = 0
            while q:


                lenQ = len(q)
                height += 1

                for _ in range(lenQ):
                    node = q.popleft()
                    visited.add(node)

                    for adj in adjMap[node]:
                        if adj not in visited:
                            q.append(adj)
            
            heights.append(height)

        minVal = min(heights)
        res = []
        for i, h in enumerate(heights):
            if h == minVal:
                res.append(i)

        return res

        
        
