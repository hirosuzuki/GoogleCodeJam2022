T = int(input())
CMYKList = []
for _ in range(T):
    CMYK3 = [[int(x) for x in input().split()] for _ in range(3)]
    CMYKList.append(CMYK3)

def solve(T, CMYKList):
    for i in range(T):
        case_no = i + 1
        print(f"Case #{case_no}:", end=" ")
        min_colors = [min(colors) for colors in zip(*CMYKList[i])]
        if sum(min_colors) < 1000000:
            print("IMPOSSIBLE")
        else:
            left = 1000000
            colors = []
            for i in range(4):
                color = min(left, min_colors[i])
                left -= color
                colors.append(color)
            print(*colors)

solve(T, CMYKList)