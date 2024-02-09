import heapq as hq


def dijkstra(graph, start):
    distances = {}
    heap = [(0, start)]

    while heap:
        dist, node = hq.heappop(heap)
        if node in distances:
            continue
        distances[node] = dist
        for neighbor, weight in graph[node].items():
            if neighbor not in distances:
                hq.heappush(heap, (dist + weight, neighbor))

    return distances


if __name__ == '__main__':
    austria_roads = {
        'Vienna': {'Linz': 125, 'Modling': 30},
        'Linz': {'Wels': 30, 'Vienna': 125},
        'Modling': {'Vienna': 30, 'Graz': 120, 'Eisenstadt': 35},
        'Wels': {'Linz': 30, 'Salzburg': 70, 'Graz': 145},
        'Salzburg': {'Innsbruk': 130, 'Villach': 145, 'Wels': 70},
        'Villach': {'Salzburg': 145, 'Klagenfurt': 30},
        'Innsbruk': {'Bregenz': 130, 'Salzburg': 130},
        'Bregenz': {'Innsbruk': 130},
        'Graz': {'Klagenfurt': 95, 'Modling': 120, 'Wels': 145},
        'Klagenfurt': {'Villach': 30, 'Graz': 95},
        'Eisenstadt': {'Modling': 35},
    }
    print(dijkstra(austria_roads, 'Vienna'))
