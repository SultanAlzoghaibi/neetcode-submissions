class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seenSet = set()

        for num in nums:
            if num in seenSet:
                return True
            else:
                seenSet.add(num)
        return False