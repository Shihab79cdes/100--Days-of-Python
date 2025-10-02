
import random

rock = """
       _______
   ---'   ____)
         (_____)
         (_____)
         (____)
   ---.__(___)
   """

paper = """
      _______
  ---'   ____)____
            ______)
            _______)
           _______)
  ---.__________)
 """

scissor = """
      _______
  ---'   ____)____
            ______)
         __________)
        (____)
  ---.__(___)

  """
user_choice = int(input("What do you chooose ? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))


option = [rock, paper, scissor]


computer_choice = random.randint(0,2)

print(f"you choose:{option[user_choice]}")
print(f"computer choose :{option[computer_choice]}")


if user_choice==computer_choice:
    print("its draw")

elif user_choice ==0 and computer_choice==2:
    print("you won")


elif user_choice==1 and computer_choice==0:
    print("you won")

elif user_choice==2 and computer_choice==1:
    print("you won")
else:
    print("you lose")
