class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = 0
        currMax = nums[0]

        for num in nums:
            currSum = max(0, currSum)
            currSum += num
            currMax = max(currMax, currSum)
        return currMax
