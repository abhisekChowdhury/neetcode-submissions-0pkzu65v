class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        course_map = defaultdict(list)
        visiting = set()
        visited = set()
        result = []

        for course, prereq in prerequisites:
            course_map[course].append(prereq)
        
        def dfs(course):
            if course in visiting:
                return False
            
            if course in visited:
                return True
            
            visiting.add(course)

            for prereq in course_map[course]:
                if not dfs(prereq):
                    return False
            
            visiting.remove(course)
            visited.add(course)
            result.append(course)

            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return result