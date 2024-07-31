def solution(data, ext, val_ext, sort_by):
    answer = []
    extIndex = {'code': 0, 'date': 1, 'maximum': 2, 'remain': 3}
    for d in data:
        if d[extIndex[ext]] < val_ext:
            answer.append(d)
    answer.sort(key = lambda x: x[extIndex[sort_by]])
    return answer