graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

def dfs(graph, start):
    stack = [start]
    visited = []
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.append(vertex)
            stack.extend(graph[vertex] - set(visited))
    return visited

def bfs(graph, start):
    queue = [start]
    visited = []
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.append(vertex)
            queue.extend(graph[vertex] - set(visited))
    return visited

def dfs(graph, start, visited=None):
    if not visited:
        visited = []
    visited.append(start)
    for next in (graph[start] - set(visited)):
        dfs(graph, next, visited)
    return visited

def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))

def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

 def shortest_dfs_path(graph, start, goal):
    possible_paths = list(dfs_paths(graph, start, goal))
    return min(possible_paths)

  def shortest_bfs_path(graph, start, goal):
    possible_paths = list(bfs_paths(graph, start, goal))
    return min(possible_paths)


