class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # linked lists where the val is Number : true / flase
        # mayb a hashmap

        seqSet = set(nums)        
        maxCount = 0

       
            
        for num in seqSet:
     
             count = 1
             if (num - 1) not in seqSet:
             
                 while (num + count) in seqSet:
                 
                    count += 1

             maxCount = max(maxCount, count)
        

        return maxCount



                