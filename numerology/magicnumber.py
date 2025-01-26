def lifepath(num):
    sum = 0
    while num > 0 or sum > 9:
        if num == 0:
            num = sum
            sum = 0
        sum += num % 10
        num //= 10
    return sum


def main():
    print("Welcome to magicnumber! Calculate your personal numerology here!")

main()
