class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #look for courses with no prereq and take those
        #courses requiring the above courses don't need prereqs anymore.
        #take the next layer of courses next requiring no prereqs
        #Repeat until everything is done (or until you're stuck - every remaining course is still waiting on something)
        # Kahn - repeatedly take whatever has nothing blocking it and cross it off everyone else's blocker list

        #in degree - for each course, how many prereqs is it still waiting on?
            #in_degree = 0 (nothing blocking. take now)
            #in_degree = 3 (still waiting on 3 things)
        #adj - for each course, what does finishing it unblock?
            #Finishing course X, look up adj[X] to know which in_degree to decrease
        
        adj = defaultdict(list)
        in_degree = [0]*numCourses

        for a,b in prerequisites:
            adj[b].append(a) # finishing b unlocks a
            in_degree[a]+=1  # course a waits on something
        
        q = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:   # first layer of no blockers
                q.append(i)         # append to q
        
        order = []

        while q:    #while no blocker courses exist in queue
            current_course = q.popleft()
            order.append(current_course)

            for blocked_course in adj[current_course]:
                in_degree[blocked_course] -= 1
                if in_degree[blocked_course] == 0:
                    q.append(blocked_course)
        
        return len(order) == numCourses


