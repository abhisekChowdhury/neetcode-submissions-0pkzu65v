class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq_map = defaultdict(list)
        visited = set()
        visiting = set()

        for course,prereq in prerequisites:
            prereq_map[course].append(prereq)
        
        def can_complete(course):
            if course in visited:
                return True
            
            if course in visiting:
                return False
            
            visiting.add(course)

            for prereq in prereq_map[course]:
                if not can_complete(prereq):
                    return False
            
            visiting.remove(course)
            visited.add(course)

            return True
        
        for course in range(numCourses):
            if not can_complete(course):
                return False
        return True