class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        '''
        adj course of prerequisites

        but the query

        dfs til you encounter the prereq from the v elemente of the search

        leverage and adjMap to then have false adj or in fact
        course:set()
        to cache we simple add ellements to the parend adjMap[parent] to speed up future queries

        3 -> 2 -> 1

        3:set(2)
        2:set(1)
        1:set()

        target = 1
        we want ->

        3:set(2,1)
        2:set(1)
        1:set()
        '''


        adjMap = defaultdict(set)

        for course, prereq in prerequisites:
            adjMap[course].add(prereq)
        
        cacheMap = adjMap

        visited = set()
       # print(cacheMap)

        def dfs(course, target):
            #print("course:", course, "target:", target, visited)

            if course == target or target in cacheMap[course]:
                #print("true")
                return True


            

            if course in visited:
                return False
            visited.add(course)


            for prereq in list(cacheMap[course]):
                if dfs(prereq, target):                 # CHANGE: stop as soon as one branch finds it
                    cacheMap[course].add(target)        # CHANGE: cache the TARGET found, not `visited`
                    return True

       

           
            return False

        res = []
        for start, target in queries:
            #print("RUN", start, target)
            res.append(dfs(start, target))
            visited.clear() 
        return res







        