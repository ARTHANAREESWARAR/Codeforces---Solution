def minimize_inversions(t, test_cases):
    results = []
    
    for i in range(t):
        n = test_cases[i][0]  # number of arrays
        arrays = test_cases[i][1]  # list of arrays
        
        # Sort the arrays based on the first element and then the second element
        arrays.sort()
        
        # Collect the result in the desired order
        result = []
        for a1, a2 in arrays:
            result.append(a1)
            result.append(a2)
        
        results.append(result)
    
    return results


# Input Reading
import sys

def main():
    input = sys.stdin.read
    data = input().splitlines()
    
    t = int(data[0])  # number of test cases
    test_cases = []
    index = 1
    
    for _ in range(t):
        n = int(data[index])  # number of arrays
        index += 1
        
        arrays = []
        for __ in range(n):
            a1, a2 = map(int, data[index].split())
            arrays.append((a1, a2))
            index += 1
            
        test_cases.append((n, arrays))
    
    # Process the test cases
    results = minimize_inversions(t, test_cases)
    
    # Output the results
    for result in results:
        print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()
