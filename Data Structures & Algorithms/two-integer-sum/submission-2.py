class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        
        for i in range(len(nums)):

            idealNum = target - nums[i]
            if idealNum in hashmap:
                return [hashmap[idealNum], i]
            else:
                hashmap[nums[i]] = i

        return False