num = input("Enter a number: ")
digit_sum = sum(int(digit) for digit in num if digit.isdigit())
print(f"The sum of the digits is: {digit_sum}")
