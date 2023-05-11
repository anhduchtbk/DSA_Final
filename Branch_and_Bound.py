import heapq

def branch_and_bound(graph, start, end):
    # Khởi tạo các giá trị ban đầu
    distances = {}
    predecessors = {}
    for node in graph:
        distances[node] = float('inf')
        predecessors[node] = None
    distances[start] = 0

    # Khởi tạo hàng đợi ưu tiên với đỉnh bắt đầu và khoảng cách 0
    pq = [(0, start)]

    # Tính toán đường đi ngắn nhất
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        if current_node == end:
            break
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))

    # Tạo đường đi từ đỉnh bắt đầu đến đỉnh kết thúc
    path = []
    node = end
    while node is not None:
        path.insert(0, node)
        node = predecessors[node]

    # Trả về đường đi ngắn nhất và chi phí của nó
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
end = 'E'

print(branch_and_bound(graph, start, end))