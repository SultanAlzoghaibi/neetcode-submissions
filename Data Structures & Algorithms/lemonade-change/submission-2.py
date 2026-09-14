class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:

        change  = {5: 0, 10: 0, 20: 0}

        for bill in bills:
            
            print(change)
            change[bill] += 1
            

            if bill == 20:
                if change[5] > 0 and change[10] > 0:
                    change[5] -= 1
                    change[10] -= 1

                elif change[5] > 2:
                    change[5] -= 3

                else:
                    print(False, bill)
                    return False
                    
            if bill == 10:
                if change[5] > 0:
                    change[5] -= 1
                
                else:
                    print(False, bill)
                    return False

        return True



            

        