def main():
    x = input().strip()

    x = list(x)  

    for i, digit in enumerate(x):
        if digit > '4':
            x[i] = chr(ord('9') - ord(digit) + ord('0'))

    if x[0] == '0':
        x[0] = '9'
    
    x = ''.join(x)  
    print(x)

if __name__ == "__main__":
    main()
