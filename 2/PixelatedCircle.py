T = int(input())

import math

def calc(R):
    cs1 = [[0] * (R*2+1) for _ in range(R*2+1)]
    cs2 = [[0] * (R*2+1) for _ in range(R*2+1)]

    def draw_circle_filled(cs, r):
        for x in range(-r, r + 1):
            for y in range(-r, r + 1):
                    if round(math.sqrt(x * x + y * y)) <= R:
                        cs[y + R][x + R] = 1

    def draw_circle_perimeter(cs, r):
        for x in range(-r, r + 1):
            y = round(math.sqrt(r * r - x * x))
            #print("*", x, y)
            cs[y + R][x + R] = 1
            cs[-y + R][x + R] = 1
            cs[x + R][y + R] = 1
            cs[x + R][-y + R] = 1

    def draw_circle_filled_wrong(cs, r):
        for x in range(0, r + 1):
            draw_circle_perimeter(cs, x)

    draw_circle_filled(cs1, R)
    draw_circle_filled_wrong(cs2, R)

    result = 0
    for r1, r2 in zip(cs1, cs2):
        for c1, c2 in zip(r1, r2):
            if c1 != c2:
                result += 1
    print(result)

    #print(*cs1, sep="\n", end="\n\n")
    #print(*cs2, sep="\n", end="\n\n")
    ...

def solve(T):
    for i in range(T):
        R = int(input())
        case_no = i + 1
        print(f"Case #{case_no}:", end=" ")
        calc(R)

solve(T)
