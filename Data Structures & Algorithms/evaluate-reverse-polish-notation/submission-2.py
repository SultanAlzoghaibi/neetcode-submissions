class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        

        OppHash = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: a / b if b != 0 else float('inf')  # handle div by 0
        }

        stk = []


        

        for token in tokens:

            if token in OppHash:
                b = stk.pop()
                a = stk.pop()
                result = int(OppHash[token](a,b))
                stk.append(result)
            else:
                stk.append(int(token))

        return stk[0]
