num = int(input("Enter a number: "))

if num % 10 == 0:
    print(f"{num} is a multiple both by 10 and 5")
elif num % 5 == 0:
    print(f"{num} is multuple by 5 but not 10.")

else:
    print(f"{num}is not multiple by 5 and 10")