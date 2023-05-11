INF = float('inf')

def bellman_ford(graph, start):
    # Khởi tạo khoảng cách từ đỉnh bắt đầu đến tất cả các đỉnh khác là vô cùng
    dist = {v: INF for v in graph}
    dist[start] = 0

    # Lặp qua tất cả các cạnh và cập nhật khoảng cách nếu cần
    for _ in range(len(graph) - 1):
        for u in graph:
            for v in graph[u]:
                if dist[u] + graph[u][v] < dist[v]:
                    dist[v] = dist[u] + graph[u][v]

    # Kiểm tra xem có chu trình âm hay không
    for u in graph:
        for v in graph[u]:
            if dist[u] + graph[u][v] < dist[v]:
                raise ValueError("Chu trình âm tồn tại!")

    return dist

graph = {
    'A': {'B': 5, 'C': 1},
    'B': {'D': 3, 'E': 6},
    'C': {'B': 2, 'D': 4},
    'D': {'E': 2},
    'E': {},
    'F': {'C': 1}
}

start = 'A'