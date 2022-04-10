T = int(input())
RC = [[int(x) for x in input().split()] for _ in range(T)]

def solve(T, RC):
    for i in range(T):
        case_no = i + 1
        r, c = RC[i]
        print(f"Case #{case_no}:")
        print(".." + "+-" * (c - 1) + "+")
        print(".." + "|." * (c - 1) + "|")
        for _ in range(r - 1):
            print("+-" + "+-" * (c - 1) + "+")
            print("|." + "|." * (c - 1) + "|")
        print("+-" + "+-" * (c - 1) + "+")


solve(T, RC)