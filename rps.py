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

#Write your code below this line 👇

combinations = [rock, paper, scissors]

inpt = int(input('What do you choose? Typ 0 for Rock, 1 for Paper or 2 for Scissors: '))

your_choice = combinations[inpt]
print(your_choice)

comp_choice = random.randint(0, len(combinations) - 1)
comp_choice_int = combinations[comp_choice]
print(f'Computer chose:\n{combinations[comp_choice]}')


if your_choice == comp_choice_int:
  print('Draw')
elif your_choice == combinations[0] and comp_choice_int == combinations[2]:
  print('You win')
elif your_choice == combinations[2] and comp_choice_int == combinations[1]:
  print('You win')
elif your_choice == combinations[1] and comp_choice_int == combinations[0]:
  print('You win')
else:
  print('You lose')
