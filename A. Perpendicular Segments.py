import sys
input = sys.stdin.read

def main():
    data = input().split()
    t = int(data[0])
    idx = 1
    results = []
    
    for _ in range(t):
        a = int(data[idx])
        b = int(data[idx + 1])
        k = int(data[idx + 2])
        idx += 3

        val = min(a, b)
        results.append(f"0 {val} {val} 0")
        results.append(f"0 0 {val} {val}")

    print("\n".join(results))

if __name__ == "__main__":
    main()
