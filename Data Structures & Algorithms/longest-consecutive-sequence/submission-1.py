class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # 
        #
        '''
        the start of a seq is when n - 1 = null
        the end is when n + 1 = null
        '''

        numSet = set(nums)
        maxSeqSize = 0
        n = 0

        for num in nums:
            SeqSize = 0
            n = num
            while n in numSet:
                SeqSize += 1
                n += 1
            
            maxSeqSize = max(maxSeqSize, SeqSize)

        return maxSeqSize