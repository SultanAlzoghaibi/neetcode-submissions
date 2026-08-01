class Solution:
    def jump(self, nums: List[int]) -> int:


        res = 0

        l = r = 0

        while r < len(nums) - 1:
            farthest = 0

            # r+1 bc the upper bound is exclusive
            for i in range(l, r + 1):
                farthest = max(farthest, nums[i] + i)
            l = r + 1 
            r = farthest
            res += 1

        return res






        