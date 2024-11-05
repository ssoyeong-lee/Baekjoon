import heapq as hq

def solution(scoville, K):
    hq.heapify(scoville)
    
    cnt = 0
    while len(scoville) >= 2 and scoville[0] < K:
        first = hq.heappop(scoville)
        second = hq.heappop(scoville)
        hq.heappush(scoville, first + second * 2)
        cnt += 1
    return cnt if scoville[0] >= K else -1