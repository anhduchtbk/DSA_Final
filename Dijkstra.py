import heapq

def dijkstra(graph, start, end):
    # Khởi tạo khoảng cách ban đầu và hàng đợi ưu tiên
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = [(0, start)]

    # Duyệt qua các đỉnh theo thứ tự ưu tiên và cập nhật khoảng cách
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if current_node == end:
            break
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    # Trả về đường đi ngắn nhất từ đỉnh bắt đầu đến đỉnh kết thúc
    path = []
    if distances[end] != float('inf'):
        node = end
        while node != start:
            path.append(node)
            node = min(graph[node], key=lambda x: distances[x] + graph[node][x])
        path.append(start)
        path.reverse()

    return path, distances[end]



graph = {
    'A': {'B': 5, 'C': 1},
    'B': {'D': 3, 'E': 6},
    'C': {'B': 2, 'D': 4},
    'D': {'E': 2},
    'E': {},
    'F': {'C': 1}
}

start = 'A'

distances = dijkstra(graph, start, end='E')
print(distances)