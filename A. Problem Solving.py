t = int(input())
for _ in range(t):
    n = int(input())
    lis = list(map(int,input().split()))
    
    lis.sort()

    if(lis[n-1] - lis[n-2] <= 2):
        print(lis[n-2])

    else:
        print("Ambiguous")
