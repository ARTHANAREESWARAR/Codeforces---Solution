t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))

    perfect = True
    for i in range(n - 1):
        interval = abs(nums[i] - nums[i + 1])
        if interval not in (5, 7):
            perfect = False
            break

    if perfect:
        print("YES")
    else:
        print("NO")
