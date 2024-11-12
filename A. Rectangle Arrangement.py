def solve():
    n = int(input())
    mx1 = mx2 = -float('inf')

    for _ in range(n):
        w, h = map(int, input().split())
        mx1 = max(mx1, w)
        mx2 = max(mx2, h)

    print(2 * (mx1 + mx2))

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        solve()
