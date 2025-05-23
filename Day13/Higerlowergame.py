#lets build a basic higher or lower game, where user need to guess whether A or B is higher if the user gets 3 points he wins



import random


instagram_celebrities = [
    {"name": "Instagram", "followers_millions": 687, "country": "USA", "industry": "Social Media Platform"},
    {"name": "Cristiano Ronaldo", "followers_millions": 652, "country": "Portugal", "industry": "Football"},
    {"name": "Lionel Messi", "followers_millions": 505, "country": "Argentina", "industry": "Football"},
    {"name": "Selena Gomez", "followers_millions": 421, "country": "USA", "industry": "Musician & Actress"},
    {"name": "Dwayne Johnson", "followers_millions": 394, "country": "USA", "industry": "Actor & Wrestler"},
    {"name": "Kylie Jenner", "followers_millions": 394, "country": "USA", "industry": "Media Personality"},
    {"name": "Ariana Grande", "followers_millions": 376, "country": "USA", "industry": "Musician & Actress"},
    {"name": "Kim Kardashian", "followers_millions": 357, "country": "USA", "industry": "Media Personality"},
    {"name": "Beyoncé", "followers_millions": 312, "country": "USA", "industry": "Musician & Actress"},
    {"name": "Khloé Kardashian", "followers_millions": 303, "country": "USA", "industry": "Media Personality"},
    {"name": "Nike", "followers_millions": 301, "country": "USA", "industry": "Sportswear Brand"},
    {"name": "Justin Bieber", "followers_millions": 294, "country": "Canada", "industry": "Musician"},
    {"name": "Kendall Jenner", "followers_millions": 288, "country": "USA", "industry": "Media Personality"},
    {"name": "Taylor Swift", "followers_millions": 282, "country": "USA", "industry": "Musician"},
    {"name": "National Geographic", "followers_millions": 279, "country": "USA", "industry": "Magazine"},
    {"name": "Virat Kohli", "followers_millions": 271, "country": "India", "industry": "Cricketer"},
    {"name": "Jennifer Lopez", "followers_millions": 249, "country": "USA", "industry": "Musician & Actress"},
    {"name": "Neymar", "followers_millions": 229, "country": "Brazil", "industry": "Football"},
    {"name": "Nicki Minaj", "followers_millions": 226, "country": "Trinidad & Tobago", "industry": "Musician"},
    {"name": "Kourtney Kardashian", "followers_millions": 219, "country": "USA", "industry": "Media Personality"},
]

score = 0

print("Lets begin the Game ")
A = ""
B = ""
A = random.choice(instagram_celebrities) 
while score < 3 :
    
    B = random.choice(instagram_celebrities)
    
    while B["name"] == A["name"] : #if both A and B are same choose a new only for B as long as both are assigned different names
        B = random.choice(instagram_celebrities)


    print("Guess Higher or Lower of the instagram celebrity : \n")

    print(f"Option A : name is {A["name"]} , Country is {A["country"]} and Industry they are working are {A["industry"]} \n ")

    print("or \n")

    print(f"Option B : name is {B["name"]} , Country is {B["country"]} and Industry they are working are {B["industry"]} \n ")


    userguess = input("Please enter your guess A or B : \n")

    if userguess == "A" :
        if A["followers_millions"] > B["followers_millions"] :

            score +=1 #increase the score as the user found the correct answer
        else:            
            print(f"YOU LOST,Score : {score}")
            break #break as the user lost 
    elif userguess == "B" :
        if B["followers_millions"] > A["followers_millions"] :
            score +=1   #break as the user lost
            A = B #Assign the B value to A for next round
        else:
            print(f"YOU LOST,Score : {score}")
            break
    else:
        print("Please enter valid input : ")


if score == 3 :
    print("You Won")