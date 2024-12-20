def solution(order):
    n = len(order)
    main_belt = [i for i in range(n, 0, -1)]
    sub_belt = []
    truck = []
    
    for o in order:
        while main_belt and main_belt[-1] < o:
            sub_belt.append(main_belt.pop())
        if main_belt and main_belt[-1] == o:
            truck.append(main_belt.pop())
        elif sub_belt and sub_belt[-1] == o:
            truck.append(sub_belt.pop())
        else:
            break
    return len(truck)
    
    