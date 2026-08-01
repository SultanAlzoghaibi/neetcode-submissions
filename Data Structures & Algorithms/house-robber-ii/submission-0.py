class Solution:
    def rob(self, nums: List[int]) -> int:

        
        return max(nums[0], self.robH(nums[1:]), 
                            self.robH(nums[:-1]))

    def robH(self, nums):
        r1, r2 = 0, 0
        
        for n in nums:
            temp = max(n + r1, r2)
            r1 = r2
            r2 = temp

        return r2
    