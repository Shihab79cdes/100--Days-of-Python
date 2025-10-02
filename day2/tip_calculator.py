# A Tip Calculator that i made by myself.

print("welcome to the tip calculator")
Bill=float(input("What was the total bill \u20b9?"))
tip_percentage=float(input("How much tip would you like to give? 12%, 10%, or 15%:"))
people=float(input("How many people to spilt the bill?"))

# CALCULATIONS
tip_amount=  tip_percentage/100*Bill
print(f"Tip amount is {tip_amount}")

total_bill=  Bill+tip_amount
print(f"Total bill is now {total_bill}")

each_people = total_bill / people

print(f"each person should pay\u20b9{each_people:.2f}")
