
def solution(a, b):
    cnt = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    date = ['FRI','SAT','SUN','MON','TUE','WED','THU']

    a -= 1
    b -= 1

    idx = (sum(cnt[:a]) + b) % 7
    return date[idx]