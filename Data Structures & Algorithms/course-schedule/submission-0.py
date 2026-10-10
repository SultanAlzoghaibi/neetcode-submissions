class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:


        visited = set()
        adjMap = defaultdict(list) # course, [prereq1, ...]

        for course, prereq in prerequisites:

            adjMap[course].append(prereq)

        print(adjMap)




        def dfs(course):

            if course in visited:
                return False              
            
            if not adjMap[course]:
                return True   

            visited.add(course)
            for preReq in adjMap[course]:
                if not dfs(preReq):
                    return False
             
            adjMap[course] = [] 
            visited.remove(course)

            return True

        
        for i in range(numCourses):
            if not dfs(i):
                return False
           

        return True