class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        '''
        k = 1

        2,1,1,3,1
        
        
        '''

        window = set()
        last = 0

        for i, n in enumerate(nums):
            if n in window: 
                return True
            window.add(n)
            if len(window) > k:
                window.remove(nums[last])
                last += 1
        return False


        
        
            


        