# brandes.py

from collections import deque, defaultdict

def brandes_betweenness_centrality(graph):

    betweenness = dict.fromkeys(graph, 0.0)

    for s in graph:
        # stack of nodes in order of non-increasing distance from s
        S = []

        # predecessors of nodes
        P = defaultdict(list)

        # number of shortest paths from s to each node
        sigma = dict.fromkeys(graph, 0.0)
        sigma[s] = 1.0

        # distance from s to each node
        dist = dict.fromkeys(graph, -1)
        dist[s] = 0

        # BFS queue
        Q = deque([s])

        # --- BFS to compute shortest paths
        while Q:
            v = Q.popleft()
            S.append(v)
            for w in graph[v]:
                # w found for the first time?
                if dist[w] < 0:
                    dist[w] = dist[v] + 1
                    Q.append(w)
                # Is this the shortest path to w?
                if dist[w] == dist[v] + 1:
                    sigma[w] += sigma[v]
                    P[w].append(v)

        # --- Accumulation
        delta = dict.fromkeys(graph, 0.0)
        while S:
            w = S.pop()
            for v in P[w]:
                delta_v = (sigma[v] / sigma[w]) * (1 + delta[w])
                delta[v] += delta_v
            if w != s:
                betweenness[w] += delta[w]

    # for undirected graphs, divide by 2
    for v in betweenness:
        betweenness[v] /= 2.0

    return betweenness


