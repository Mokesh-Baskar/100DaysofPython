# lets create a function where multiple function is present where one function is argument to another 
#mutiple return function where more than one item can be returned

import random
def my_func():

    randomword = ["apple","grape","orange","guava"]

    randomkey = ["1","2","3","4"]

    selectedword = random.choice(randomword)
    selectedkey = random.choice(randomkey)

    return selectedword,selectedkey



my_word, my_key = my_func()

# system will assign the values based ont eh position it returned and the variable position in the declaartion

print(f"my selected word and selected key are {my_word} , {my_key}")