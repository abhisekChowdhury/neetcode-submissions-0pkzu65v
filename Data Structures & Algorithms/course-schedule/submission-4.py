class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_map = defaultdict(list)
        visiting = set() # course is currently being looked at
        visited = set() # course has been checked and marked safe

        for course, prereq in prerequisites:
            course_map[course].append(prereq)

        def finish_possibility(course):
            if course in visiting:
                return False
            
            if course in visited:
                return True
            
            visiting.add(course)

            for prereq in course_map[course]:
                if not finish_possibility(prereq):
                    return False
            
            visiting.remove(course) #remove from visiting
            visited.add(course) #mark as safe
        
            return True
        
        for i in range(numCourses):
            if not finish_possibility(i):
                return False
        return True