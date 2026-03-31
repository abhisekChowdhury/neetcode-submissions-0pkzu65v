class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i:[] for i in range(numCourses)}

        for course, prereq in prerequisites:
            graph[course].append(prereq)
        
        visited = set()
        visiting = set()
        result = []

        def dfs(course):
            if course in visiting:
                return False
            if course in visited:
                return True
            
            visiting.add(course)

            for prereq in graph[course]:
                if not dfs(prereq):
                    return False
            
            visiting.remove(course)
            visited.add(course)
            result.append(course)

            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []
            # else:
            #     result.add(visited)
        
        return result