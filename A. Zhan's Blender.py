T = int(input())  # Number of test cases
for _ in range(T):
    n = int(input())  # Number of fruits
    x, y = map(int, input().split())  # Number of fruits Zhan can put in blender, blender capacity per second
    
    if n == 0:
        print(0)  # If no fruits, no time needed
    else:
        # We need to check how many fruits can be blended per second
        min_blend = min(x, y)
        
        # Compute the minimum time required
        time_required = (n + min_blend - 1) // min_blend  # Ceiling division
        
        print(time_required)
