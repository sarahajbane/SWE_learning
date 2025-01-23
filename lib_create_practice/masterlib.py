def sum_of_digits(num):
    sum = 0
    for digit in str(num):
      sum += int(digit)
    return sum

def sum_to_single_digit(num):
    sum = 0
    while num > 0 or sum > 9:
        if num == 0:
            num = sum
            sum = 0
        sum += num % 10
        num //= 10
    return sum


def main():
    print("Welcome to masterlib library! Enjoy your usage!")

main()