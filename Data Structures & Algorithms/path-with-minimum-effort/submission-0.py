class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # edges -> u: [(v,w),...)
        # minheap -> (w,u) where w is culmative of total weight to get there


        DIRECTION = [(-1,0),(1,0),(0,-1),(0,1)]
        ROWS = len(heights)
        COLS = len(heights[0])
        edges = defaultdict(list)
      
        for r in range(ROWS):
            for c in range(COLS):

                for moveR, moveC in DIRECTION:
                    newR = r + moveR
                    newC = c + moveC
                    if 0 <= newR < ROWS and 0<= newC < COLS:
                        edges[(r,c)].append(((newR, newC), abs(heights[r][c] - heights[newR][newC])))

        minHeap = [(0,(0,0))]

        heapq.heapify(minHeap)
        effort = 0
        visited = set()

        #print(edges)
        while minHeap:

            w1, n1 = heapq.heappop(minHeap)
            if n1 in visited:
                continue
            visited.add(n1)
            effort = max(effort, w1)

            if n1 == (ROWS-1, COLS-1):
                return w1


            for n2, w2 in edges[n1]:
               
                if n2 in visited:
                    continue
                heapq.heappush(minHeap, (max(w1,w2), n2))

        return effort if len(visited) == len(edges) else -1




                