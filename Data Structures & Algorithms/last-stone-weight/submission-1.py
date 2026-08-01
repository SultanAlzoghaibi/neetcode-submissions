class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-s for s in stones]
        
         
        heapq.heapify(maxHeap)
        
        while len(maxHeap) > 1:
            x = -1 * heapq.heappop(maxHeap)
            y = -1 * heapq.heappop(maxHeap)
            if x < y:
                y -= x
                heapq.heappush(maxHeap, y * -1)
            elif y < x:
                x -= y
                heapq.heappush(maxHeap, x * -1)

            heapq.heapify(maxHeap)

        if not maxHeap:
            return 0

        return -1 * maxHeap[0]
            