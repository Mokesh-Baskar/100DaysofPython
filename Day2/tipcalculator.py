

bill = int(input("Please enter the total bill  amount : $ "))

percentage = int(input("Please enter the tip percentage i.e 10 , 15 , 20 :"))


Totalbillwithtip = float((percentage/100) * bill + bill)

print(f"Total bill amount ot be paid is ${Totalbillwithtip}")