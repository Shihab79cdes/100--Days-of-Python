# A Tip Calculator 

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





# ANOTHER METHOD IN SHORT
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))


#calculation

total_bill_with_tip = (bill * tip/100) + bill

spilt_people = round(total_bill_with_tip / people,2)

print(f" each person should pay ${spilt_people}")
