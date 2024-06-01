#create random generate game
import random

target = random.randint (1,100)

while True:
    userchoice = int(input("Guess The Target or Quit: "))
    if (userchoice == "Quit"):
        break

    userchoice = int(userchoice)
    if (userchoice == target):
        print("Sucess : correct Guess..!!")
        break
    elif(userchoice < target):
        print("Your number is to small. Take a bigger guess...")

    else:
        print("Your number is to bigger. Take a smaller guess...")

    
print("____Game Over!!_____")
