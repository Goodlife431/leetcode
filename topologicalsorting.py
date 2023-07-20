# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.

class solution(object):
    def can_finish(num_courses, prerequisities):
        graph = defaultdict(list)
        in_degree = [0] * num_courses

        for courses, preq in prerequisities:
            graph[preq].append(courses)
            in_degree[courses] += 1
            
        queue = deque()
        for course in range (num_courses):
            if in_degree[courses] == 0:
                queue.append(course)
        
        count = 0
        while queue:
            node = node.popleft()
            count += 1

            for neighbour in graph[node]:
                in_degree[neighbour] -= 1
                if in_degree[neighbour] == 0:
                    queue.append(neighbour)

        return count == num_courses


