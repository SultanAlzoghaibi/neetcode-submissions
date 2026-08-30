class Solution:
    def simplifyPath(self, path: str) -> str:

        """
        
        /a/./b

        """
        stk = [] #folder1, folder 2
        
        parts = path.split('/')
       
        
        for part in parts:
            if part == "" or part == ".":
                continue
            elif part == "..":
                if stk:
                    stk.pop()
            else:
                stk.append(part)
        print(stk)
        return "/" + "/".join(stk)



        