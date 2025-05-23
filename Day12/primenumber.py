#Basic prime number checker 

def is_prime(num):
    
    if num == 1 :
        return False
    elif num == 2:
        return True
    else:
        for i in range(2,num):
            if num%i == 0 :
                return False
        
        return True


num = int(input("Enter the number : "))


result = is_prime(num)

if result == True :
    print("Is a Prime")
else:
    print("Not a Prime")    