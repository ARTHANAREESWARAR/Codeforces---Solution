def solve():
    size = int(input())
    for _ in range(size - 1):
        print('0', end='')
    print('1')

def main():
    test_cases = int(input())
    for _ in range(test_cases):
        solve()

if __name__ == "__main__":
    main()
