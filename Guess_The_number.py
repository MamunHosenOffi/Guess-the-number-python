import random

target = random.randint(1,100) #randint use for int number

#print(target) : Know about the exact number

while True:
    userChoice = int(input("Guess the target : "))

    if userChoice == target:
        print("Congratulations, You guess the right number")
        break
    elif userChoice < target:
        print("That's not right...Guess again.. , You need Bigger number")
    else:
        print("Oopss... Guess again.. , You need smaller number")
print("-----Game Over-----")