T = int(input())

def calc(xs):
    result = 0
    l = 0
    r = len(xs) - 1
    x = 0
    while l <= r:
        # print(xs[l:r+1], l, r, x, result)
        if xs[l] < xs[r]:
            y = xs[l]
            l += 1
        else:
            y = xs[r]
            r -= 1
        if y >= x:
            result += 1
            x = y
    return result


def solve(T):
    for i in range(T):
        N = int(input())
        xs = [int(x) for x in input().split()]
        case_no = i + 1
        print(f"Case #{case_no}:", end=" ")
        print(calc(xs))

solve(T)
