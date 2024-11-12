def minimum_bulbs(t, test_cases):
    results = []
    for k in test_cases:
        # The minimum number of bulbs needed is 2 * k - 1
        results.append(2 * k - 1)
    return results

# Input reading
t = int(input())
test_cases = [int(input()) for _ in range(t)]

# Get the results
results = minimum_bulbs(t, test_cases)

# Output results
for result in results:
    print(result)
