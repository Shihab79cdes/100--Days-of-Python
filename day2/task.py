# DATA TYPES, NUMBERS, OPERATIONS, TYPE CONVERSION, f-strings.


# subscripting (means to take the list of strings from their specific position) *it may be in positive form,
# by starting from 0,1,2,3etc. and in negative form (starting -1,-2,-3etc)

# print("shihab"[0])  #output -- 's'
# print ("shihab"[-1]) - output-- 'b'

# strings
# print("1230"+"234") #output - 1230234 (#this is concatenation it will just merge the numbers instead of "adding".)

# int (integers) = all whole numbers no matters positive or negetive are called integers in programming.
# print( 1230 + 234 ) output -1464 (#this will print the calculated number, as its not strings.)

# large numbers
# print(456123_789)  # by giving underscore. #output - 456123789

# Float = Floating Point Number (because it has a decimal place.)
# print(3.7987) #output--3.7987

# Bollean (it is most used data types in programming) *this value is always begin with capital T and F, and they dont have any quotation.
# print (True)
# print (False)


# Lets talk about more Data types and function
# Note 1. Len function not work with integers it will give type error
# len(6677) output-- it will show 'type error'

# For knowing data types (we use (type) function)
# print(type("shihab"))  #output - 'str' it means string data type.
# print(type(123))  #output - 'int'    it means integer data type.
# print(type(234.45)) #output - 'float'  data type is float.
# print(type(True)) #output - 'bool'  data type is bolean


# Now what if we aren't happy with the assigned data type ?
# If we want to convert a piece of data into a different data type?


# Than we would need to learn about something called 'TYPE CONVERSION' , also known as type casting.

# print("123" +"456") so this is a string
# what if For converting this string into integer.
# we can use one of the built-in functions called "int" for coverting into a number
# let see
# print(int("123")+ int("456")) #output- 579 (so this is the power of TYPE COVERSION)

# print("Number of letters in your name: "+len(input("Enter your name"))) #learn the type error what it means and solve it.
# lets see now.

# break kore bojano hoche

# name_of_the_user = input("enter your name")
# length_of_name =len(name_of_the_user)

# print("number of letters in your name: " + str(length_of_name))

# long e emon vabe
# print("Number of letters in your name: "+ str (len(input("Enter your name"))))


# a =23
# c=46
# print(str(a)+ "+" +str(c))


# MATHEMATICAL OPERATION IN PYTHON

# print(123+344) #additon
# print(123-344) #subtraction
# print(4*5)# multiply
# print(type(6/3)) #divide but the answer is coming in float.so for that
# print(6 // 3) #for removing decimal point. so use it carefully.
# print(2**3) #exponent the power is last digit.


# PENDAS OR BODMAS

# ()
# **
# *
# /
# +
# -
# simplify
# print(3 * (3 + 3) / 3 - 3)

# BMI calculator
# math formula -- BMI= weight/(height*height)
# TO calculate in python = bmi= weight / height**2

# weight=84
# height=1.65
# find bmi
# bmi= 84 / 1.65**2
# print(bmi)
# print(int(bmi)) #to removing the decimal point.
# print(round(bmi)) #to get the ans in round we use (round) function
# print(round(bmi,2)) #for getting the number in round of 2 digit
# by using f string the round off style will change that is--- {:.2f} for 2 digit.

# user scores a point
# score= 2
# score +=1
# print(score)

# f-strings
# score= 2
# height=3.44
# is_winning=True

# print(f" your score is {score}, your height is {height}, your winning is {is_winning}")


# print(6+4/2-(1*2))


# a= int("5") / int(2.7)

# print(a)
# age=str(int(12))
# print("you are "+age+" years old")


# final project
# A Tip Calculator

# number=input("Enter a number")
# print (type(number))


# print("Welcome to tip calculator")
# bill=float(input("What was the total bill? $ "))
# tip=int(input("How much tip would you like to give?10,12,15?"))
# spilt=int(input("How many people to spilt the bill?"))

# tip_as_percent= tip/ 100
# total_tip_amount= bill * tip_as_percent
# total_bill= bill + total_tip_amount
# bill_per_person= total_bill / spilt
# finsl_smount= round(bill_per_person,2)
# print(f"Each person should pay: ${finsl_smount}")


# Tip calculator i made myself.
# \u20b9 for rupees symbol

# print("welcome to the tip calculator")
# Bill=float(input("What was the total bill \u20b9?"))
# tip_percentage=float(input("How much tip would you like to give? 12%, 10%, or 15%:"))
# people=float(input("How many people to spilt the bill?"))
# # to calculate
# # step 1
# tip_amount=  tip_percentage/100*Bill
# print(f"Tip amount is {tip_amount}")

# total_bill=  Bill+tip_amount
# print(f"Total bill is now {total_bill}")

# each_people = total_bill / people

# print(f"each person should pay\u20b9{each_people:.2f}")


# MY self task.
# Calculate simple interest

# principal_amount=float(input("Say the principal amount? \u20b9"))
# rate=float(input("Rate of interest:10,12,15 ="))
# time=float(input("what is the time period?-" ))

# # calculation
# si= principal_amount * rate * time/100
# print(f"your total interest is {si :.2f}")

# amnt=si + principal_amount
# total_amount=input("would you want the total amount in bank?")
# print(f"the total amount is \u20B9 {amnt}")


# important

# subscripting mane holo square bracket diye kumo string/ list er index access kora.
# print("hello"[4])


# print(bool("1212") + bool("333"))


# SOLUTION

#  step 1
# 👉 Python e kono non-empty string always True hoy.


# bool("1212") ➝ True
# bool("333")  ➝ True


# Step 2: True + True
# Python e True = 1 and False = 0
# So:
# python
#
# True + True = 1 + 1 = 2

# step3
# print(bool("1212") + bool("333"))  # Output: 2


# name = input("what is your name?")

# print(f"hello,{name}")


# name = input("what is your name?")
# print("hello," + name)

# age = 12

# print(f"you are {age} years old")

