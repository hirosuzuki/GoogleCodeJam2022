T = int(input())

def calc(N, K):
    r = N*N-1-K
    m = (N-1)*4-2
    rs = set()
    while m > 0 and len(rs) < K:
        if r >= m:
            rs.add(m)
            r -= m
            m -= 8
        else:
            m -= 2
    if r != 0:
        print("IMPOSSIBLE")
        return
    #print("*2", rs)
    a = []
    c = -1
    while rs:
        for i in range(4):
            w = c * 8 + i * 2
            wn1 = (c*2+1)**2+c+1 + (i*(c+1)*2)
            wn2 = ((c+1)*2+1)**2+(c+1)+1 + (i*(c+2)*2)
            n1 = N*N + 1 - wn1
            n2 = N*N + 1 - wn2
            d = n1 - n2 - 1
            #print(c, i, wn1, wn2, n1, n2, d)
            if d in rs:
                a.append((n2, n1))
                rs.remove(d)
        c += 1
    print(len(a))
    for x, y in a[::-1]:
        print(x, y)


def solve(T):
    for i in range(T):
        N, K = [int(x) for x in input().split()]
        case_no = i + 1
        print(f"Case #{case_no}:", end=" ")
        calc(N, K)

solve(T)
