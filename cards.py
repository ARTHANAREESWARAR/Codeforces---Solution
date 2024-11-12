def solve():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    
    max_element = float('-inf')
    for x in arr:
        max_element = max(max_element, x)
    
    total_sum = sum(arr)
    
    for i in range(n, 0, -1):
        quotient = (total_sum + k) // i
        
        if quotient * i < total_sum:
            continue
        
        if quotient <= max_element:
            continue
        
        print(i)
        return


def main():
    test_cases = int(input())
    
    for _ in range(test_cases):
        solve()


if __name__ == "__main__":
    main()
