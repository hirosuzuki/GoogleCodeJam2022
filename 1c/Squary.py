T = int(input())

import sys
sys.setrecursionlimit(10000)


def calc(N, K, E):
    if K == 1:
        s1 = sum(E)
        s2 = sum(x**2 for x in E)
        if s1 == 0 and s2 == 0:
            return "1"
        if s1 == 0:
            return "IMPOSSIBLE"
        if (s2 - s1**2) % (s1*2) != 0:
            return "IMPOSSIBLE"
        r = (s2 - s1**2) // (s1*2)
        return f"{r}"
    
    s1 = sum(E)
    s2 = sum(x**2 for x in E)
    if s1**2 == s2:
        return 0
    #print(E, s1, s2)

    E.append(1 - s1)
    s1 = sum(E)
    s2 = sum(x**2 for x in E)
    d = s2 - s1**2
    #print(E, s1, s2, d)
    if d % 2 == 1:
        return "IMPOSSIBLE"
    E.append(d//2)
    s1 = sum(E)
    s2 = sum(x**2 for x in E)
    d = s2 - s1**2
    #print(E, s1, s2, d)
    return " ".join(str(x) for x in E[-2:])

def solve(T):
    for i in range(T):
        N, K = [int(x) for x in input().split()]
        E = [int(x) for x in input().split()]
        case_no = i + 1
        print(f"Case #{case_no}:", end=" ")
        print(calc(N, K, E))

solve(T)
