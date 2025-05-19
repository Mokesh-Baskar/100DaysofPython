#lets take a look into a unique datatype in python named dictionary 
#dictionaary is defined with {} braces and works as a Key value pair eg: "fruit":"Apple". Where fruit is key and apple is value
#dictionary doesnt have indices like list and items with the dictionary can be accessed based on their key i.e fruit

my_dict = {
    "fruit" : "apple",
    "pet":"dog",
    "game":"cricket"
}


#printing the entier dictionary
print(my_dict)

#prinitng a specific value based on key
print(my_dict["fruit"])

#amednding a value of a key

my_dict["game"] = "hockey"

#lets print the amended name

print(my_dict["game"])

#lets loop throught he dictionary

for favorites in my_dict:
    print(favorites)

#the above code will print only the key because python will loop through the key items only

for favs in my_dict:
    print(my_dict[favs])    

#dictionary wont have duplicate values so it will behave like sets where there will be unique keys
#the keys in dictioanry must be immutable like int,str,float
#there is a immutable datatype in python named tuple which we can see later
#the main reason for using immutable is that dictionary keys must be hashable, where as other like list are mutable so it cannot be used (Seems pretty advanced for now, lets check this later)
 
