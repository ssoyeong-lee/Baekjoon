from collections import defaultdict

def solution(genres, plays):
    total = defaultdict(int)
    songNum = defaultdict(list)

    for i in range(len(genres)):
        total[genres[i]] += plays[i]
        songNum[genres[i]].append([i, plays[i]])
    rank = sorted(total, key=lambda x: -total[x])

    ret = []
    for genr in rank:
        song_per_genr = sorted(songNum[genr], key=lambda x:(-x[1], x[0]))
        for num, cnt in song_per_genr[:2]:
            ret.append(num)
    
    return ret