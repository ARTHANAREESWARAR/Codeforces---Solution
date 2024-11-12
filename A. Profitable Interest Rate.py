t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    
    if a >= b:
        print(a)  
    else:
        max_x = 2*a - b
        print(max(max_x, 0))
