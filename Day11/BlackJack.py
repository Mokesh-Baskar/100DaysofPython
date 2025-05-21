#Lets create a programm for Black Jack game

# refer to this link for rules
#https://casinomentor.com/blackjack-guides/rules-of-blackjack-570
#lets keeps this game simple , where the dealer deals the card to the players and when it exceeds 21 they are eliminated 

import random

cardstack = [11,2,3,4,5,6,7,8,9,10,10,10,10] 

dealerhand = []
Playerhand = []

def begingame(playerhand,sum):
    
    while sum <22 :

        hit=input("Please enter Hit for a Card")

        if hit == "Hit" :
            playerhand.append(random.choice(cardstack))
            sum+=playerhand[-1]
            print(f"Card Dealt to Player is {playerhand[-1]} and sum is {sum}")
            print(*playerhand)
        else :
            print("Player chose for stand")
            break
    if sum >21 :
        print("You lost")
        return playerhand,sum
    else :
        print("lets raise the dealer hand ")
        return playerhand,sum

for i in range(1,3):
    dealerhand.append(random.choice(cardstack))
    Playerhand.append(random.choice(cardstack))

print(f"Cards currently in Player's hand is {Playerhand[0]} and {Playerhand[1]} ")

print(f"Cards currently in Dealer's hand revealed is {dealerhand[0]} ")
Sum = Playerhand[0]+Playerhand[1]
print(f"sum of the Player's card is {Sum} ")

if Sum > 21 :
    print("YOU LOSE")
else :
    Playerhand,Sum = begingame(Playerhand,sum)

Dealersum = dealerhand[0]+dealerhand[1]



