class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) < 2:
            return nums[0]


        dp1, dp2 = nums[0], max(nums[0], nums[1]) 

        for num in nums[2:]:
            dp1, dp2 = dp2, max(dp1 + num, dp2)

        return dp2
        