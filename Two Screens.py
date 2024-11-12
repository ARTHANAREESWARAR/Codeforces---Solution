def find_minimum_time(s, t):
    
    i = 0
    while i < len(s) and i < len(t) and s[i] == t[i]:
        i += 1
    
    
    prefix = i
    
    
    r1 = len(s) - prefix
    r2 = len(t) - prefix
    
    
    return len(s) + len(t) if prefix == 0 else prefix + 1 + r1 + r2


t = int(input())

for _ in range(t):
    
    s = input().strip()
    t = input().strip()
    
    
    print(find_minimum_time(s, t))
