

#lets consider the BMI calcualor and say the person is in what range

weight =float(input("Enter weight in kg : "))

height = float(input("Enter height in meter : "))

height = height
bmi = weight / height**2

#basic if else statement where we can check another condition in else staement as well
if bmi>25:
    print("you are obese")
elif bmi < 20:
    print("You are lean")
elif bmi>=20 or bmi<=25 : 
    print("You are perfect")


