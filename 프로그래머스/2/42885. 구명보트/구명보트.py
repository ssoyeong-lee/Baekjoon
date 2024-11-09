def solution(people, limit):
    people.sort()
    
    cnt = 0
    first, second = 0, len(people) - 1
    while first <= second:
        if people[first] + people[second] <= limit:
            first += 1
        second -= 1
        cnt += 1
    return cnt