import sys

input = lambda: sys.stdin.readline().rstrip()  # Faster input handling

def solve_case():
    n = int(input())
    a = list(map(int, input().split()))

    ans = 0
    # Loop to compare pairs
    for i in range(1, (n + 1) // 2):
        j = n - 1 - i
        # Calculate options based on equality of pairs
        opt1 = int(a[i] == a[i - 1]) + int(a[j] == a[j + 1])
        opt2 = int(a[i] == a[j + 1]) + int(a[j] == a[i - 1])
        ans += min(opt1, opt2)

    # If n is even, check the middle elements
    if n % 2 == 0:
        ans += int(a[n // 2] == a[n // 2 - 1])
    
    return ans

# Process multiple test cases
ans = []
for _ in range(int(input())):
    ans.append(str(solve_case()))

# Print all results
print("\n".join(ans))
