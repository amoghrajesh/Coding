def cycle(prerequisites, numCourses):
    graph = dict()
    for i in range(numCourses):
        graph[i] = []

    visited = [False]*numCourses
    recStack = [False]*numCourses

    for v1, v2 in prerequisites:
        graph[v1].append(v2)


    def detectCycle(v):
        visited[v] = True
        recStack[v] = True
        for adj in graph[v]:
            if visited[adj] == False:
                if detectCycle(adj) == True:
                    return True
            else:
                if recStack[adj] == True:
                    return True
        recStack[v] = False
        return False




    for node in range(numCourses):
        if visited[node]==False:
            if detectCycle(node) == True:
                return True
    return False

numCourses = 2
prerequisites = [[1,0]]
print(cycle(prerequisites, numCourses))