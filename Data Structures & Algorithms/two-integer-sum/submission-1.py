class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for n in range(len(nums)):
            m = target - int(nums[n])
            if m in nums:
                pos_m = nums.index(m)
                
                if pos_m != n:
                    if pos_m > n:
                        return [n,pos_m]
                    return [pos_m,n]
                    