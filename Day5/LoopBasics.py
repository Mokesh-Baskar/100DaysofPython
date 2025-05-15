
#python has loop operations where it can loop through a list to do a operation ot find a item in the list for example

fruits = ["Banana","Cherry","Mango","Grape","Stawberry","lichi"]

#we can loop through the items and print them one by one , where i holds teh value one by one looping through
for i in fruits:
    print( i )


#We can use range to loop to n times

for i in range(0,6):
    print(fruits[i])

#Lets create a max score finder 

scores =[92,94,81,51,62,72,91]
max_score =0

for i in scores:

    if max_score < i:
        max_score = i


print( f"Maximum score in the list is {max_score}"  )     


# there is another loop named while loop wheere the program will lopp aslong as the rule is passing 
counter = len(fruits) - 1
while counter >= 0:
    print(fruits[counter])
    counter-=1   


