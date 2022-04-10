T = int(input())

from errno import EEXIST
import sys
sys.setrecursionlimit(10000)
from collections import defaultdict

stack_cache = {}

def all_stacks(xs):
    if sum(xs) == 0:
        return [""]
    if xs in stack_cache:
        return stack_cache[xs]
    rs = []
    for i, v in enumerate(xs):
        if v > 0:
            lxs = tuple([b - (j == i) for j, b in enumerate(xs)])
            for c in all_stacks(lxs):
                r = str(i) + c
                rs.append(r)
    stack_cache[xs] = rs
    return rs

#d_cache = {}

def calc_d(r, t):
    #k = (r, t)
    #if k in d_cache:
    #    return d_cache[k]
    l = 0
    for c1, c2 in zip(r, t):
        if c1 != c2:
            break
        l += 1
        
    result = len(r) - l + len(t) - l
    #d_cache[k] = result
    return result

def calc_dist(r, rs):
    result = 1000000000000
    for t in rs:
        rr = calc_d(r, t) + rs[t]
        result = min(result, rr)
    return result

def calc(E, W, X):
    rs = defaultdict(int)
    rs[""] = 0
    for i in range(E):
        ixs = all_stacks(X[i])
        nrs = defaultdict(int)
        for r in ixs:
            nrs[r] = calc_dist(r, rs)
        rs = nrs
    r = min(rs[k] for k in rs) + sum(X[-1])
    return r

def solve(T):
    for i in range(T):
        E, W = [int(x) for x in input().split()]
        if E > 10 or W > 3:
            return
        X = [tuple([int(x) for x in input().split()]) for i in range(E)]
        case_no = i + 1
        print(f"Case #{case_no}:", end=" ")
        print(calc(E, W, X))

solve(T)
