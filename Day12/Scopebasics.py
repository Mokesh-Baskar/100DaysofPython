#Lets gets some hands on concept of Scope. 
# There are two types local and Global 


Globalnumber = 10

Globalnumber+=1

#there is concept named Global constants
#Constants in Python are defined in caps

PI = 3.14

# even though they are contants program can cahnge the value as python doesnt force immutablity. Its a understanding such variables hould not be changed

# constants can be accessed anywhere in the file

#the below print will print the Global number as 11
print(Globalnumber)


def localscope():
    #the below Global number has local scope so that its different from the variable present outside the function
    Globalnumber = 8
    #the below print will print he vaue as 3
    print(Globalnumber)
    #constants can be accessed anywhere
    print(PI)

localscope()

#The below print will priht the value as 11 even though its changed as 3 in the function because the GlobalNumber variable in localscopre function is different and has only local scope

print(Globalnumber)


#There is a keyword to access the global scope variable inside a function and amend the values globally

def localtoglobal():

    global Globalnumber

    Globalnumber = 3

localtoglobal()

#now the global variable is accessble to the function and the value is amended

print(Globalnumber)



#block scope is not present in python
#Whenever a variable is defined inside a code block like if and for its accesseble outside the code block


for i in range(0,3) :
    print("for loop is running")



print(i)

