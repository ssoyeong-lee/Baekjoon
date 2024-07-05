import heapq as hq

MAXLEN = 100000

n, k = map(int, input().split())
visited = [False] * (MAXLEN + 1)


def bfs(n, k):
    heap = [(0, n)]
    visited[n] = True

    while heap:
        # print(heap)
        dist, now = hq.heappop(heap)
        if now == k:
            return dist
        i = now * 2
        while 0 < i <= MAXLEN:
            if not visited[i]:
                hq.heappush(heap, (dist, i))
                visited[i] = True
            i *= 2
        if 0 <= now - 1 and not visited[now - 1]:
            visited[now - 1] = True
            hq.heappush(heap, (dist + 1, now - 1))
        if now + 1 <= MAXLEN and not visited[now + 1]:
            visited[now + 1] = True
            hq.heappush(heap, (dist + 1, now + 1))


if n == k:
    print(0)
else:
    print(bfs(n, k))
