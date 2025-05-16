

#lets create a password by calling a function
#lets reuse the setup from previous classes

import random

#lets create a random password generator for the user based ont he input



Userinputlength=input("Please enter the size of the password you wish  :)  8 to 16 is sweet spot ")


def passwordgenerator(inputlength):

    alphabets = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    alphabetscaps = ["A","B","C","D","E","F","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    Symbols = ["!","@","#","$","%","^","&","*","(",")","+","="]
    password =""
    for i in range(1,int(inputlength)+1):
    #lets user random lib to select items randomly form the list
        if (i)%3 ==0 : #lets use modulo and select the list  from which itemns must be selected
            positionindex = random.randint(0,len(Symbols)-1)
            password = password + Symbols[positionindex]
        elif  (i)%3 ==1:   
            positionindex = random.randint(0,len(alphabets)-1)
            password = password + alphabets[positionindex]
        else:
            positionindex = random.randint(0,len(alphabetscaps)-1)
            password = password + alphabetscaps[positionindex]
#return function can be used to send back the password made out of the scope to be assigned in a variable
    return(password)        


mynewpassword = passwordgenerator(Userinputlength)


print(mynewpassword)