import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

RPS_list = [rock, paper, scissors]
print("0 for rock, 1 for paper, 2 for scissors.")
user_choice = int(input("3,2,1, SHOOT!\n"))
rand_choice = random.randrange(0,3)
print("You chose:\n" + RPS_list[user_choice])
print("Computer chose:\n" + RPS_list[rand_choice])
if user_choice == rand_choice:
    print("tie game!")
elif user_choice == 0:
    if rand_choice == 1:
        print("LOSER")
    else:
        print("nice")
elif user_choice == 1:
    if rand_choice == 2:
        print("LOSER")
    else:
        print("nice")
else:
    if rand_choice == 0:
        print("LOSER")
    else:
        print("nice")