T = int(input())
F = []
P = []
for _ in range(T):
    _ = input()
    F.append([int(x) for x in input().split()])
    P.append([int(x) for x in input().split()])

from collections import defaultdict
from sys import setrecursionlimit

setrecursionlimit(100010)

def calc(F, P):
    rs = defaultdict(set)
    for i, n in enumerate(P):
        rs[n].add(i + 1)
    
    def calc_tree(n):
        cur_fun = F[n - 1] if n >= 1 else 0
        total_score = 0
        total_min_fun = 0
        for r in rs[n]:
            score, min_fun = calc_tree(r)
            total_score += score
            if total_min_fun > min_fun or total_min_fun == 0:
                total_min_fun = min_fun
        if total_min_fun < cur_fun:
            total_score += cur_fun - total_min_fun
            total_min_fun = cur_fun
        return total_score, total_min_fun

    result, min_fun = calc_tree(0)
    return result

def solve(T, F, P):
    for i in range(T):
        case_no = i + 1
        print(f"Case #{case_no}:", calc(F[i], P[i]))

solve(T, F, P)
