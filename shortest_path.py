
import heapq
from collections import defaultdict

class Solution:
    def shortestPath(self, n, edges, labels, k):
        graph = [[] for _ in range(n)]

        for u, v, w in edges:
            graph[u].append((v, w))

        # dist[node][count] = minimum distance
        dist = [[float('inf')] * (k + 1) for _ in range(n)]

        # Starting node has one occurrence of its label
        dist[0][1] = 0

        pq = [(0, 0, 1)]

        while pq:
            cost, node, count = heapq.heappop(pq)

            if cost != dist[node][count]:
                continue

            if node == n - 1:
                return cost

            for nxt, weight in graph[node]:
                if labels[nxt] == labels[node]:
                    new_count = count + 1
                else:
                    new_count = 1

                if new_count > k:
                    continue

                new_cost = cost + weight

                if new_cost < dist[nxt][new_count]:
                    dist[nxt][new_count] = new_cost
                    heapq.heappush(
                        pq, (new_cost, nxt, new_count)
                    )

        return -1
