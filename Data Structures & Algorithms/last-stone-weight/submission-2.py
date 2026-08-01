class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-stone for stone in stones]

        heapq.heapify(maxHeap)


        while len(maxHeap) > 1:
            x = -1 * heapq.heappop(maxHeap)
            y = -1 * heapq.heappop(maxHeap)

            if x > y:
                newX = x - y
                newX *= -1
                heapq.heappush(maxHeap, newX)

        
        if len(maxHeap) == 0:
            return 0

        return -1 * heapq.heappop(maxHeap)
        

