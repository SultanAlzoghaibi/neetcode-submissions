class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # iteraive if num found return
        l = 0
        r = len(nums) - 1
        n = 0
        
        while l <= r:
            mid = (l + r) // 2
            n += 1
            print(f"l: {l}")
            print(f"r: {r}")
            print(f"mid: {mid}")
            print(f"nums[mid]: {nums[mid]}")
        
            if nums[mid] == target:
                print(f"returning: {mid}")
                return mid

            elif nums[mid] < target:
                l = mid + 1
            
            else:
                r = mid - 1
            
            
            

            


        return -1