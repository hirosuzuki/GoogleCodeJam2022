T = int(input())

import sys
import os

def case():
    r = 0
    while True:
        if r == 0:
            req = "00000000"
        elif r == 8:
            req = "11111111"
        else:
            req = "1" * (8 - r) + "0" * r

        # print(f"< {req}", file=sys.stderr)
        print(req)
        sys.stdout.flush()
        r = int(input())
        # print(f"> {r}", file=sys.stderr)
        if r == 0:
            return
        if r == -1:
            os.exit(-1)

def solve(T):
    for i in range(T):
        case()

solve(T)
