def can(arr, n):
    sum_idx_map = {}
    curr_sum = 0
    segment_count = 0
    last_end = -1

    sum_idx_map[0] = -1

    for i in range(n):
        curr_sum += arr[i]

        if curr_sum in sum_idx_map:
            prev_idx = sum_idx_map[curr_sum]

            if prev_idx >= last_end:
                segment_count += 1
                last_end = i

        sum_idx_map[curr_sum] = i

    return segment_count


def main():
    t = int(input())

    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))

        print(can(arr, n))


if __name__ == "__main__":
    main()
