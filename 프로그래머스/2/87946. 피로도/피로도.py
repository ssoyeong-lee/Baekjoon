answer = -1
def bt(k, dungeons, visited):
    global answer
    
    answer = max(answer, len(visited))
    for i in range(len(dungeons)):
        if i not in visited and k >= dungeons[i][0]:
            visited.add(i)
            bt(k - dungeons[i][1], dungeons, visited)
            visited.remove(i)

def solution(k, dungeons):
    bt(k, dungeons, set())
    return answer