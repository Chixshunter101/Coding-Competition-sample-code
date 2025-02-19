weigth = int(input("Enter your weigth: "))
unit = input("Kilogram or Pounds?(K or L): ")
if unit == "K":
    weigth = weigth * 2.205
    unit = "Lbs."
    print(f"Your weigth is: {weigth} {unit}")  
elif unit == "L":
    weigth = weigth /  2.205
    unit = "Kgs."
    print(f"Your weigth is: {weigth} {unit}") 
else:
    print(f"{unit} was not valid")       
