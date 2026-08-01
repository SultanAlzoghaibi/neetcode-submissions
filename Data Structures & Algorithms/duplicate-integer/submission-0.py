class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        i = 0
        s_nums = sorted(nums)
        for n in s_nums:
            if i>0:
                if n == m:
                    return True
            i =+1
            m = n
        return False
        
         