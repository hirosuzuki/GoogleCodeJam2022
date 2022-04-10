import sys

def log(s):
    print(s, file=sys.stderr)

ds = [2**29] * 20 + [2**(29-i) for i in range(30)]

nums = []
n = 1
i = 0
while i < len(ds):
    m = n + ds[i]
    if m in nums or n in nums:
        n += 1
        continue
    nums += [n, m]
    i += 1

T = int(input())

for _ in range(T):
    N = int(input())
    print(*nums)
    sys.stdout.flush()

    bs = [int(x) for x in input().split()]
    bs = sorted(bs)
    pairs = [(bs[i], bs[i + 1]) for i in range(0, 100, 2)]
    pairs = sorted(pairs, key=lambda x:x[1]-x[0], reverse=True)

    bs1 = []
    bs2 = []
    for n1, n2 in pairs:
        if n1 > n2:
            n1, n2 = n2, n1
        if sum(bs1) < sum(bs2):
            bs1 += [n2]
            bs2 += [n1]
        else:
            bs1 += [n1]
            bs2 += [n2]

    for i in range(0, 100, 2):
        n1, n2 = nums[i:i+2]
        if n1 > n2:
            n1, n2 = n2, n1
        if sum(bs1) < sum(bs2):
            bs1 += [n2]
            bs2 += [n1]
        else:
            bs1 += [n1]
            bs2 += [n2]

    print(*bs1)
    sys.stdout.flush()
