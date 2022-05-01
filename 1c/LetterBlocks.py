T = int(input())

import sys
sys.setrecursionlimit(10000)

CHARS = "ABCDEFGHIJKLMNOPQRSTVWXYZ"

def calc1(xs):
    os = {}
    for x in xs:
        for i in range(len(x) - 1):
            for j in range(i + 1, len(x)):
                c1 = x[i]
                c2 = x[j]
                if c1 == c2:
                    continue
                k1 = (c1, c2)
                k2 = (c2, c1)
                if k1 in os:
                    if os[k1] != True:
                        return "IMPOSSIBLE"
                os[k1] = True
                if k2 in os:
                    if os[k2] != False:
                        return "IMPOSSIBLE"
                os[k2] = False
    return "-"

def calc(xs):
    ws = {}
    for x in xs:
        c = x[0]
        if c not in ws:
            ws[c] = ""
        if x[-1] == c:
            ws[c] = x + ws[c]
        else:
            ws[c] += x
    f = True
    while f:
        f = False
        for k in list(ws.keys()):
            v = ws[k]
            c = v[-1] 
            if k != c and c in ws:
                ws[k] = v + ws[c]
                del ws[c]
                f = True
                break
    r = "".join(ws[k] for k in ws)

    cs = set(r[0])
    for i in range(1, len(r)):
        p = r[i - 1]
        c = r[i]
        if p != c:
            if c in cs:
                return "IMPOSSIBLE"
            cs.add(c)

    return r


def solve(T):
    for i in range(T):
        N = int(input())
        xs = [x for x in input().split()]
        case_no = i + 1
        print(f"Case #{case_no}:", end=" ")
        print(calc(xs))

solve(T)
