def sum_of_digits(num):
    sum = 0
    for digit in str(num):
      sum += int(digit)
    return sum

def sum_to_single_digit(num):
    sum = 0
    for digit in str(num):
        sum += int(digit)
    while 0 <= sum <= 9:
        for digit in str(sum):
            sum += int(digit)
    return sum


def main():
    print("Welcome to masterlib library! Enjoy your usage!")

main()