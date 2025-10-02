# 1. List of LETTERS, NUMBERS AND SYMBOLS (PASSWORD INGREDIENTS)
import random

letters = ['a', 'b', 'c', 'd','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers =['0','1','2','3','4','5','6','7','8','9']
symbols =['!', '#', '$', '%', '&','*','+']

# 2. Welcome message and user input
print("welcome to the Pypassword Generator!")
nr_letters =int(input("How many letters would you like in your password?\n"))
nr_symbols= int(input("How many symbols would you like?\n"))
nr_numbers =int(input("How many numbers would you like?\n"))

# # easy level
# 2. PASSWORD CREATION
password =" "

for character in range(0, nr_letters ):
    password+= random.choice(letters)


for character in range(0, nr_symbols):
    password+= random.choice(symbols)

for character in range(0, nr_numbers):
    password+= random.choice(numbers)
print(password)




# HARD LEVEL PASSWORD.
import random

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "*", "+"]

# 2. Welcome message and user input
print("welcome to the Pypassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

password_list = []

for character in range(0, nr_letters):
    password_list.append ( random.choice(letters))


for character in range(0, nr_symbols):
    password_list.append ( random.choice(symbols))

for character in range(0, nr_numbers):
    password_list.append( random.choice(numbers))

random.shuffle(password_list)

password= ""
for character in password_list:
    password+=character
print(f"your password is :{password}")

