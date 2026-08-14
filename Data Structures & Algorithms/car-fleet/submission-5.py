class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        


            # if topCar speed < target - pos
            # //
            # ( target - pos) // speed = step
            # 
            positionToSpeed = {}
            for i in range(len(speed)):
                positionToSpeed[position[i]] = speed[i]


            position.sort()

            if len(position) == 0:
                return 0
            #print(target, position[-1], positionToSpeed[position[-1]])
            
            stk = [(target - position[-1]) / positionToSpeed[position[-1]]]

            #print(stk, stk[-1], (target - position[-1]), positionToSpeed[position[-1]])

            for i in range(len(position) - 2, -1, -1):
               
                aheadCar = stk[-1]

                currCar = (target - position[i]) / positionToSpeed[position[i]]

                #print(stk, currCar, (target - position[i]), positionToSpeed[position[i]], "|", "pos:", position[i],"speed:", positionToSpeed[position[i]], "steps:", currCar)

                if currCar <= aheadCar:
                    pass
                else:
                    stk.append(currCar)
            
            return len(stk)

