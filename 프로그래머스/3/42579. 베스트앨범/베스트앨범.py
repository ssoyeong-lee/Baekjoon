from collections import defaultdict

def solution(genres, plays):
    total = defaultdict(int)
    li = defaultdict(list)
    for i in range(len(genres)):
        total[genres[i]] += plays[i]
        li[genres[i]].append([i, plays[i]])
    
    tmp = []
    for t in total.keys():
        tmp.append([t, total[t]])
    total = sorted(tmp, key=lambda x:-x[1])
    
    ret = []
    for genr, a in total:
        tmp = li[genr]
        tmp.sort(key=lambda x:(-x[1], x[0]))
        
        for i in range(min(2, len(tmp))):
            ret.append(tmp[i][0])
    
    return ret