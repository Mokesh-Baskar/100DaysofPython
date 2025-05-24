#lets create a coffeemachine program which takes order from the user, verifies the amount paid. Pays back the remianing change. maintains the resources available in the machine to make cofee

#cosntant with data regarding the resources needed to make coffee
DATA = {
    "espresso":{
            "milk" : 18,
            "water": 50,
            "coffee": 0,
            "price": 1.50
    }
    ,"cappucino":{
            "milk" : 100,
            "water": 250,
            "coffee": 24,
            "price": 3.00
    }
    ,
    "latte":{
            "milk" : 150,
            "water": 200,
            "coffee": 24,
            "price": 2.5
    }
}

#data redgarding  the resources available in the machine
coffeemachine_data = {
            "milk" : 1000,
            "water": 500,
            "coffee": 500,
            "money": 0
}

#value of the coins
COIN_DATA = {

            "penny" : 0.01,
            "nickel": 0.05,
            "dime": 0.10,
            "quater": 0.25
}

#common sequence where we compare the required resources and add up the card value
def checkoutsequence(order):
        cartvalue = 0
        if DATA[order]["milk"] < coffeemachine_data["milk"] and DATA[order]["water"] < coffeemachine_data["water"] and DATA[order]["coffee"] < coffeemachine_data["coffee"] :
            
            for  i in COIN_DATA :
                cartvalue+= int(input(f"please enter no of {i} : ")) * COIN_DATA[i]
            if cartvalue == DATA[order]["price"] :
                coffeemachine_data["money"] += cartvalue
                print("Thanks for your order, enjoy your coffee")
            elif cartvalue > DATA[order]["price"]:
                coffeemachine_data["money"] += DATA[order]["price"]
                print(f"Here is your change ${round(cartvalue - DATA[order]["price"],3)}")
                print("Thanks for your order, enjoy your coffee")
            else:    
                print(f"Need additional ${cartvalue - DATA[order]["price"]}")
                print("Take your money in dispenser")
            #adjusting the values in the coffemachine 
            coffeemachine_data["milk"] -= DATA[order]["milk"] 
            coffeemachine_data["water"]-=  DATA[order]["water"]   
            coffeemachine_data["coffee"]-= DATA[order]["coffee"] 
        else:
            print("Sorry for the inconvinence, Enough resources not available to take this order")

def reportsequence() :
        print(f"Amount of milk in machine : {coffeemachine_data["milk"]}ml")
        print(f"Amount of water in machine : {coffeemachine_data["water"]}ml")
        print(f"Amount of coffee in machine : {coffeemachine_data["coffee"]}g")
        print(f"Amount of money in machine : ${coffeemachine_data["money"]}")
boot = input("Booting up the system, Need report or start sequence :")


if boot == "report" :
    reportsequence()
elif boot == "start" :
    while boot == "start" :
        order = input("Please enter your order (espresso/latte/cappucino) : ")
        
        if order == "espresso" :
            checkoutsequence(order)
        elif order == "latte" :
            checkoutsequence(order)
        elif order == "cappucino" :
            checkoutsequence(order)
        elif  order == "report" :
            reportsequence()
        elif order == "shutdown" :
            print("Shutting down the machine")
            boot = "stop"    