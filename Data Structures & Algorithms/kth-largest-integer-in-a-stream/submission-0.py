
import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = nums
        heapq.heapify(self.minHeap)


        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap) # remove the gibest element

    def add(self, val: int) -> int:
        # adding
        heapq.heappush(self.minHeap, val) 
        # returning
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0] 


        
