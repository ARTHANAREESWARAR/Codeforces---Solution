t = int(input())
for _ in range(t):
    round_number = []
    x = int(input())
    s = str(x)

    for i in range(len(s)):
        digit = int(s[len(s) - 1 - i])
        if digit != 0:
            round_number.append(digit * (10 ** i))

    print(len(round_number))
    print(*round_number)