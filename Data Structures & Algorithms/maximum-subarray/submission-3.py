class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        res = nums[0]
        currSum = nums[0]
        '''
        if currSum < 0:
            resete curr sum
        chekc the res and currSum ever loop
        '''

        for n in nums[1:]:
            
           
            if currSum < 0:
                currSum = 0
            currSum += n

            res = max(res, currSum)
        

        return res