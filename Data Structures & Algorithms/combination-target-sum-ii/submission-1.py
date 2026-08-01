class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        

        res = []
        nums = candidates 
        nums.sort()
        def dfs(i, curr, total):
            
            
            if total == target:
                res.append(curr.copy())
                return
            if total > target or i > len(nums) - 1:
                return
            
            
            curr.append(nums[i])
            dfs(i + 1, curr, total + nums[i])
            

            if i < len(nums) - 1:
                try:
                    while nums[i] == nums[i + 1]:
                        i += 1
                except:
                    return

           
                    
            curr.pop()
            dfs(i + 1, curr, total)

        dfs(0, [], 0)
        return res
        