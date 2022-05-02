T = int(input())

def calc(xs):
    rs = {0: 0}
    for cs in xs:
        cs.sort()
        nrs = {}
        nrs[cs[0]] = cs[-1] - cs[0] + min(abs(cs[-1] - k) + rs[k] for k in rs)
        nrs[cs[-1]] = cs[-1] - cs[0] + min(abs(cs[0] - k) + rs[k] for k in rs)
        rs = nrs
    result = min(rs.values())
    return result


def solve(T):
    for i in range(T):
        N, P = [int(x) for x in input().split()]
        xs = [[int(x) for x in input().split()] for _ in range(N)]
        case_no = i + 1
        print(f"Case #{case_no}:", end=" ")
        print(calc(xs))

solve(T)
