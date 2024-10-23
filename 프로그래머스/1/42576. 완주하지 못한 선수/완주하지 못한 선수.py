from collections import defaultdict
def solution(participant, completion):
    compt = defaultdict(int)
    for cc in completion:
        compt[cc] += 1
    
    for p in participant:
        if compt[p] == 0:
            return p
        compt[p] -= 1
    return ''