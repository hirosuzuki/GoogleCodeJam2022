T = int(input())
N = []
S = []
for _ in range(T):
    N += [int(input())]
    S += [[int(x) for x in input().split()]]

def calc(S):
    #if len(S) > 20:
    #    return -1
    dices = sorted(S)
    c = 0
    i = 0
    while i < len(S):
        if dices[i] >= c + 1:
            c += 1
        i += 1
    return c

def solve(T, N, S):
    for i in range(T):
        case_no = i + 1
        print(f"Case #{case_no}:", calc(S[i]))

solve(T, N, S)