class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        stk = []
        res = []


        def backtracking(openN, closedN):

            if openN == closedN == n:
                res.append("".join(stk))
                return

            if openN < n:
                stk.append("(")
                backtracking(openN + 1,closedN )
                stk.pop()

            if openN > closedN:
                stk.append(")")
                backtracking(openN ,closedN  + 1)
                stk.pop()
        
        backtracking(0,0)

        return res
