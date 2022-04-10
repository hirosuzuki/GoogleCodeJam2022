T = int(input())

import sys
sys.setrecursionlimit(10000)

def calc(s):
    # print("calc", s)
    if len(s) == 1:
        return s
    c = calc(s[1:])
    s1 = s[0] + c
    s2 = s[0] * 2 + c
    if s1 < s2:
        return s1
    else:
        return s2

def solve(T):
    for i in range(T):
        S = input()
        case_no = i + 1
        print(f"Case #{case_no}:", end=" ")
        print(calc(S))

solve(T)
