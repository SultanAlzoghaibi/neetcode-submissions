class Solution:
    def jump(self, nums: List[int]) -> int:

        goal = len(nums)
        count = 0
        l,r = 0,0
        if goal == 1:
            return 0


        while r < goal :
            print("lol")
            
            tempMax = [0, 0] # index, num
            
            while r <= l + nums[l] and r < goal:
                if tempMax[1] < nums[r] + r:
                    tempMax = [r, nums[r]]
                r += 1
            
            count += 1
            print(count)
            l = tempMax[0]
        
        return count

        