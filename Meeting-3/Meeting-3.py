from pydoc import text

friends_list = ['Amanda', 'Bruno', 'Camila', 'Drake', 'Elvis', 'Freddie', 'George', 'Harry', 'Tggy', 'Joji']

# for i in friends_list:
#     print(i)

# for i in range(3):
#     print(friends_list[i])

# for i in range(1, 11, 2):  # start from 1, ends in 11 and Increment : means : i = i+2
#     print(friends_list[i])

"""Python Conditional"""

allowance = 10
spending = 8

# print(allowance < spending)
# print(allowance > spending)
# print(allowance != spending)
# print(allowance == spending)

# print((allowance == 10) and (spending == 8))
# print((allowance == 12) or (spending == 8))

students_name = ['Alex', 'Bryan', 'Christ', 'Dave', 'Eva']
students_score = [100, 75, 80, 78, 99]
students_grade = []

for i in students_score:
    if (i >= 90):
        students_grade.append('A')

    elif (i >= 70):
        students_grade.append('B')

    else:
        students_grade.append('C')

# print(students_grade)

# while True:
#     answer = input("""Do you want to loop this argument?
#     Type yes or no: """)
#     if answer.lower() == "yes":
#          print("Okay let's go!")
#     else:
#          print("Good bye...")
#         break

"""One Liner"""

name = ['josh', 'james', 'jeo', 'jim']
# [print(i) for i in name]

score = 90
# print('A') if score >= 90 else print('B') if score >= 80 else print('C')

text = "I am learning python"

# for i in range(3):
#     print(text)

# [print(text) for i in range(3)]

import random
score = 0
player_name = input("Please enter your name: ")

while True:

    words = ["python", "computer", "programming", "condition", "else", "break", "input", "print", "while", "for"]
    pick = random.choice(words)

    random_word = random.sample(pick, len(pick))
    jumbled = "".join(random_word)
    print(("Jumbled word is :", jumbled))

    answer = input("What is in your mind? ")

    if answer == pick:
        score += 1
        print("Your score is :", score)

        if score == 10:
            print(("Congratulation", player_name, "you win!"))
            print(("Your score is :", score))

    else:
        print("Better luck next time... correct answer is :", pick)

        cont = input("Press 'y' to continue and 'n' to quit : ")
        if cont == 'n':
            print(player_name, "Your score s :", score)
            print("Thanks for playing...")
            break





