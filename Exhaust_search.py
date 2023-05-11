import itertools

def exhaustive_search(graph, start, end):
    # Tìm tất cả các đường đi có thể
    all_paths = list(itertools.permutations(graph.keys(), len(graph)))

    # Lưu trữ đường đi ngắn nhất và khoảng cách tương ứng
    shortest_path = None
    shortest_distance = float('inf')

    # Duyệt qua tất cả các đường đi và tìm đường đi ngắn nhất
    for path in all_paths:
        if path[0] != start or path[-1] != end:
            continue
        distance = 0
        for i in range(len(path)-1):
            if path[i+1] not in graph[path[i]]:
                break
            distance += graph[path[i]][path[i+1]]
        else:
            if distance < shortest_distance:
                shortest_distance = distance
                shortest_path = list(path)
    
    # Trả về đường đi ngắn nhất và khoảng cách tương ứng
    return shortest_path, shortest_distance

graph = {
    'A': {'B': 5, 'C': 1},
    'B': {'A': 5, 'C': 2, 'D': 1},
    'C': {'A': 1, 'B': 2, 'D': 4},
    'D': {'B': 1, 'C': 4}
}

print(exhaustive_search(graph, 'A', 'D'))