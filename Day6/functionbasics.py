
#lets start with functions , which are a major part of coding where reuseablity made possible


#there are few inbuilt function which we are already using without giving a secong thought 
#example print staement

print("This is a function")


#we can create custom function with our logic as well


def my_function():
    print("my custom function")


# we need a code to call the function 

my_function()


#we can pass arguments to the function to do changes with them 


a = int(15)


def my_mathfunction( i):
    print(f"{i} is printed inside the function")


#reason for making the  function call below definition is python is a run time compiler so the definition must be always above the function call
my_mathfunction(a)
