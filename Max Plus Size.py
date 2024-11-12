def max_score(nums, n, temp):
    max_val = 0
    count = 0
    for i in range(temp, n, 2):
        max_val = max(max_val, nums[i])
        count += 1
    return max_val + count

t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    sc1 = max_score(nums, n, 0)
    sc2 = max_score(nums, n, 1)
    print(max(sc1, sc2))
