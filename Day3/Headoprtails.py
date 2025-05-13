#lets create a head or tails game 

# get input from user either head or tail

# random input to choose head or tail by computer and say the user win or lose

import random
userinput = input("Enter head or tails (^;^)  : ")

computerinput = random.randint(0,1)
if userinput != "head" and userinput != "tails" :
    print("please enter either head or tails")
elif userinput == "head" and computerinput == 1 or userinput == "tails" and computerinput == 0  :
    print("You won")
else:
    print("Hard Luck You lose")