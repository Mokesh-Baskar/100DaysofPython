#lets apply the previous concepts to create a fun game which is Hangman .
#The rules of game is simple where the users need to guess the word , each failure will make teh man figure to get hanged

import random
# below list has the entry of all the countries in the world
countries = [
    "Norway", "India", "Saint Vincent and the Grenadines", "Madagascar", "Burundi", "Eritrea", "Liechtenstein", "Cuba", "Taiwan", "Switzerland",
    "Venezuela", "Tunisia", "Papua New Guinea", "Germany", "Democratic Republic of the Congo", "Palestine State", "Argentina", "San Marino", "Algeria", "Chad",
    "Malta", "Qatar", "Ecuador", "Haiti", "Somalia", "Lithuania", "Cameroon", "Russia", "Panama", "Nepal",
    "Japan", "Romania", "North Macedonia", "New Zealand", "Australia", "Benin", "Guinea", "Singapore", "Portugal", "Saudi Arabia",
    "Burkina Faso", "Moldova", "Slovakia", "Saint Lucia", "Sweden", "Indonesia", "Tajikistan", "Colombia", "Canada", "Costa Rica",
    "Pakistan", "Paraguay", "Liberia", "France", "Micronesia", "United Kingdom", "Oman", "Malawi", "Bangladesh", "South Korea",
    "Iceland", "Trinidad and Tobago", "Estonia", "Mexico", "Bulgaria", "Yemen", "Montenegro", "United States", "Sri Lanka", "Fiji",
    "Belarus", "Djibouti", "Ireland", "Afghanistan", "Uzbekistan", "Kazakhstan", "Mauritania", "South Sudan", "Myanmar", "Gabon",
    "Hungary", "Slovenia", "Eswatini", "Lebanon", "Timor-Leste", "China", "Vatican City", "Niger", "Brazil", "Mozambique",
    "Poland", "Jamaica", "Bhutan", "Kenya", "Spain", "Uganda", "Netherlands", "Angola", "Ukraine", "Tanzania",
    "Morocco", "Belgium", "Saint Kitts and Nevis", "Mauritius", "Denmark", "Seychelles", "Gambia", "Kuwait", "Czech Republic", "Latvia",
    "El Salvador", "Dominican Republic", "Tonga", "Burundi", "Zimbabwe", "Ethiopia", "Botswana", "Senegal", "Maldives", "Chile",
    "United Arab Emirates", "Georgia", "Bolivia", "Grenada", "South Africa", "Peru", "Bosnia and Herzegovina", "Marshall Islands", "Nicaragua", "Cyprus",
    "Albania", "Brunei", "Guinea-Bissau", "Comoros", "Namibia", "Suriname", "Mongolia", "Turkmenistan", "North Korea", "Uzbekistan",
    "Equatorial Guinea", "Zambia", "Thailand", "Bahrain", "Philippines", "Kiribati", "Samoa", "Togo", "Ecuador", "Central African Republic",
    "Turkey", "Solomon Islands", "Vanuatu", "Lesotho", "Luxembourg", "Sudan", "Iran", "Laos", "Cabo Verde", "Honduras",
    "Serbia", "Botswana", "Ghana", "Bosnia and Herzegovina", "Armenia", "Greece", "Fiji", "Guatemala", "Belize", "Sweden",
    "Israel", "Rwanda", "Jordan", "Dominica", "Chad", "Sierra Leone", "Burundi", "Tunisia", "Libya", "Iraq"
]


#Lets choose a random entry from the list 


#variables to store the random word, length of the word, n o of tries is equal to length of the word
Chosenword = random.choice(countries).lower()
length_of_word = len(Chosenword)
length_of_word_1 = length_of_word
no_of_tries = length_of_word

#Remove this line so that answer wont be shown prior . this is for testing purpose
print(Chosenword)

guess =[]

for j in range(0,length_of_word) :
    guess.append("_")
#*listname is a inbuilt function where the list items are printed without the brackets    
print(*guess)

#Loop should end when the User exaust all the guesses or he found the word
while no_of_tries >0 and length_of_word_1 >0 :
    
    #input from the user one by one letter
    Letter = input(f"Please enter the next guess , still {no_of_tries} left : " ).lower()
    
    found =""
    i=""

    #lets loop through the chosenword and check the input letter is present 
    for i in range(0,length_of_word) :
        
        if Letter == Chosenword[i] :            
            guess[i] = Letter
            found = 1
            #if a letter is found reduce the to be found letter count so that loop can be broken when all letters are found 
            length_of_word_1-=1 
    #if wrong guess has been done then reduce the no of guesses
    if found != 1 :
        no_of_tries-=1
        print("You lost a guess ")
        print(*guess)
    else:
        #if a letter is found then print the updated guess list
        print("You guessed correctly ")
        print(*guess)


#converting a list of letters toa  string
answer =""
for l in range(0,len(guess)):
    answer +=guess[l] 


if no_of_tries == 0 :
    print("You lost")
else:
    print("You found the word " + answer)    

#note:there is a bug in the code try to find it 


    



