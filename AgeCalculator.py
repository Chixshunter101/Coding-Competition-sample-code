from datetime import datetime

current_year = datetime.now().year

birth_year = int(input("Enter your birth year: "))
age = current_year - birth_year
print(f"You are {age}yrs old")