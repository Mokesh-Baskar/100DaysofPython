#Lets create a programm for Black Jack game

# refer to this link for rules
#https://casinomentor.com/blackjack-guides/rules-of-blackjack-570
#lets keeps this game simple , where the dealer deals the card to the players and when it exceeds 21 they are eliminated 

import random

cardstack = [11,2,3,4,5,6,7,8,9,10,10,10,10] 

dealerhand = []
Playerhand = []

def begingame(playerhand,Playersum):
    
    while (Playersum < 22) :

        hit=input("Please enter Hit for a Card : ")

        if hit == "Hit" :
            playerhand.append(random.choice(cardstack))
            if playerhand[-1] == 11 and Playersum+ playerhand[-1] >21 :
                print("Since Player's Sum goes more than 21 , Considering Ace as 1 ")
                playerhand[-1] = 1
            Playersum+=playerhand[-1]
            print(f"Card Dealt to Player is {playerhand[-1]} and Playersum is {Playersum}")
            print(*playerhand)
        else :
            print("Player chose for stand")
            break
    if Playersum >21 :
        print("You lost")
        return Playerhand , 0
    else :
        print("lets raise the dealer hand ")
        return playerhand,Playersum

for i in range(1,3):
    dealerhand.append(random.choice(cardstack))
    Playerhand.append(random.choice(cardstack))

print(f"Cards currently in Player's hand is {Playerhand[0]} and {Playerhand[1]} ")

print(f"Cards currently in Dealer's hand revealed is {dealerhand[0]} ")

if Playerhand[0] ==11 and Playerhand[1] ==11 :
    print (" You have both cards as Ace , considering it as 11 and 1")
    Playerhand[1] = 1


Playersum = Playerhand[0]+Playerhand[1]
print(f"Sum of the Player's card is {Playersum} ")

Playerhand,Playersum = begingame(Playerhand,Playersum)

if Playersum != 0:

    print(f"Dealer revealing the second card , the cards in Dealer hand are {dealerhand[0]} and {dealerhand[1]}")

    Dealersum = dealerhand[0]+dealerhand[1]

    if Dealersum < 17 :
        while Dealersum < 17 :
            print("Sum in dealers hand is less than 17 , Deals himself a card ")

            dealerhand.append(random.choice(cardstack))

            if dealerhand[-1] == 11 and Dealersum >21 :
                dealerhand[-1] = 1
            
            print(f"Card chose by dealer is {dealerhand[-1]}")

            print(f"Cards in dealers hand are")
            print(*dealerhand)

            Dealersum+=dealerhand[-1]

    if Dealersum> 21 :
        print("Dealer is Bust , You Win")
    elif Dealersum > Playersum :
        print("Dealer win")
    elif Dealersum == Playersum:
        print("Player Win")
    else:
        print("Player Win")                



