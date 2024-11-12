import math

def lcm(x:int,y:int) -> int:
    return x*y // math.gcd(x,y)


def main():
    input_strip = input().strip()
    x,y = map(input,input_strip.split())

    result = lcm(x,y)

    print(result)


if __name__ == "__main__":
    main()