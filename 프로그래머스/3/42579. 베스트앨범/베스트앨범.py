from collections import defaultdict

def solution(genres, plays):
    total = defaultdict(int)
    songNum = defaultdict(list)

    for i in range(len(genres)):
        total[genres[i]] += plays[i]
        songNum[genres[i]].append([i, plays[i]])
    
    total_list = []
    for t in total.keys():
        total_list.append([t, total[t]])
    total = sorted(total_list, key=lambda x:-x[1])
    
    ret = []
    for genr, a in total:
        song_per_genr = sorted(songNum[genr], key=lambda x:(-x[1], x[0]))
        for num, cnt in song_per_genr[:2]:
            ret.append(num)
    
    return ret