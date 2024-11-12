def can():
    n = int(input())
    switch = list(map(int, input().split()))
    num_off = switch.count(0)
    num_on = switch.count(1)

    if num_off == 0:
        print("0 0")
    else:
        if num_off >= num_on:
            print(num_off % 2, num_on)
        else:
            print(num_on % 2, num_off)


t = int(input())
for _ in range(t):
    can()
