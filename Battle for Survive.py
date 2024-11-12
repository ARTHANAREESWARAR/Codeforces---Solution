
T = int(input())

for _ in range(T):
   n = int(input())
   mp = list(map(int,input().split()))
   sm = 0
   for i in range(n):
    if i < n-2:
        sm += mp[i]

   print(mp[n-1] - mp[n-2] + sm)

    

    

    
        
    
    
