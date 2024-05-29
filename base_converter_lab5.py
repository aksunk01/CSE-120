def binary(num):
    if num == 0 or num == 1:
        return str(num)
    else:
        return binary(num//2) + str(num%2)

if __name__ == '__main__':
    num = int(input("Enter the number you want to convert: "))
    print(binary(num))