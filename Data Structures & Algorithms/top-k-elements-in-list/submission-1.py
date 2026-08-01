class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        heap = []
        heapq.heapify(heap)
        for num, cnt in count.items():
            heapq.heappush(heap, [-cnt, num])
        
        print(heap)
        res = []
        for _ in range(k):
            arr = heapq.heappop(heap) 

            res.append(arr[1])

        return res


            


            
            

