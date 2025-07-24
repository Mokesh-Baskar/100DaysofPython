import pandas
import turtle

data = pandas.read_csv("Weather_Data.csv")

print(data)

dat_dict = data.to_dict()

print(dat_dict)

Temparature = dat_dict["Temp_C"]

print(Temparature)

listoftemp = data["Temp_C"].to_list()

print(listoftemp)

print(data.Temp_C)

print(data[data.Temp_C == data.Temp_C.max()])



Squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250722.csv")

furcolor =  Squirrel_data.Primary_Fur_Color

Specific = Squirrel_data[Squirrel_data.Age == "Adult"]

print(furcolor)

print(Specific)

screen = turtle.Screen()

screen.setup(600,600)
image = "blank_states_img.gif"
screen.addshape(image)

Score = 0
Scoreboard = turtle.Turtle()
Scoreboard.penup()
Scoreboard.hideturtle()
Scoreboard.goto(0,250)
Scoreboard.write(f"Score : {Score}", align="center", font=("Verdana", 18, "bold"))

screen.title(f"Score : {Score}")

t = turtle.Turtle()
t.penup()
t.shape(image)
s= turtle.Turtle()
s.penup()
s.hideturtle()
Gameon = True
states_data = pandas.read_csv("50_states.csv")
while Gameon == True:
    guess = screen.textinput("Enter your guess","Start with capital")

    guess_xaxis = states_data[states_data.state==guess].x
    guess_yaxis = states_data[states_data.state==guess].y

    if not guess_xaxis.empty  and not guess_yaxis.empty  :
        s.goto(int(guess_xaxis.iloc[0]),int(guess_yaxis.iloc[0]))
        s.write(guess, align="center", font=("Verdana", 12, "normal"))
        Score+=1
        Scoreboard.clear()
        Scoreboard.write(f"Score : {Score}", align="center", font=("Verdana", 18, "bold"))
    else:
        Scoreboard.clear()
        Scoreboard.write(f"You Guessed wrong your Score : {Score}", align="center", font=("Verdana", 18, "bold"))
        Gameon = False


screen.exitonclick()




