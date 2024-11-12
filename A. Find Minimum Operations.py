t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    
    if k == 1:
        print(n)
    else:
        op = 0
        while n > 0:
            op += n % k
            n //= k
        print(op)
