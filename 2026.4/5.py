import heapq

num_test_cases = int(input())

for case_num in range(1, num_test_cases + 1):
    num_lairs = int(input())

    matrix = []
    tokens = []
    for _ in range(num_lairs):
        while len(tokens) < num_lairs:
            tokens.extend(input().split())
        matrix.append([int(x) for x in tokens[:num_lairs]])
        tokens = tokens[num_lairs:]

    visited = [False] * num_lairs
    min_heap = [(0, 0)]
    total_distance = 0
    connected = 0

    while min_heap and connected < num_lairs:
        dist, u = heapq.heappop(min_heap)

        if visited[u]:
            continue

        visited[u] = True
        total_distance += dist
        connected += 1

        for v in range(num_lairs):
            if not visited[v]:
                heapq.heappush(min_heap, (matrix[u][v], v))

    print(f"Case #{case_num}: {total_distance}")
