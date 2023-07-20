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


