t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    l = a[0]
    r = a[-1]
    score = (r - l) * (n - 1)
    print(score)
