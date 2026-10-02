class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq_map = defaultdict(list)
        visited = set()
        visiting = set()
        result = []

        for course, prereq in prerequisites:
            prereq_map[course].append(prereq)
        
        def completable(course):
            if course in visited:
                return True
            
            if course in visiting:
                return False
            
            visiting.add(course)
            
            for prereq in prereq_map[course]:
                if not completable(prereq):
                    return False
            
            if course not in result:
                result.append(course)

            visiting.remove(course)
            visited.add(course)

            return True
        
        for course_idx in range(numCourses):
            if not completable(course_idx):
                return []
            
        return result