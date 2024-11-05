import heapq as hq

def solution(jobs):
    n = len(jobs)
    hq.heapify(jobs)
    
    cur = 0; pq = []; cnt = 0; ret = 0
    while cnt < n:
        while jobs and cur >= jobs[0][0]:
            t, d = hq.heappop(jobs)
            hq.heappush(pq, [d, t])
        if jobs and not pq:
            cur = jobs[0][0]
            continue
        d, t = hq.heappop(pq)
        ret += cur - t + d
        cur += d
        cnt += 1
    return ret // n
            
        