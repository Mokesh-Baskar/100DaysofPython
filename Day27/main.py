import pandas



#list Comprehension

#Squaring of numbers using list comprehension


numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [n**2 for n in numbers]
print(squared_numbers)



#converting the string to numbers new list and creating a list with even numbers
list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(n) for n in list_of_strings]
result = [i for i in numbers if i%2 == 0]
print(result)



#accessing a text file and creating list from this

with open("./file1.txt") as file1:
    data1 = file1.readlines()
    value1 = [int(v.strip()) for v in data1] 
with open("./file2.txt") as file2:
    data2 = file2.readlines()
    value2 = [int(v.strip()) for v in data2]

result = [n for n in value1 if n in value2]
print(result)



#Comprehention for dictionary


#convert the sentence inlist of words
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

word_list = sentence.split()


result = {word:len(word) for word in word_list}



#Temperature conversion using dictionary comprehention
weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

weather_f = {key:round((value*(9/5)+32),1) for (key,value) in weather_c.items()}

print(weather_f)



#Name game


Name  = input("Enter your name : ").upper()



letters = [i for i in Name]

print(letters)


nato_data = pandas.read_csv("./nato_phonetic_alphabet.csv")

proxy = [nato_data[nato_data.letter == l]["code"].iloc[0] for l in letters] 

print(proxy)



#there is snother way of converting datacdv to dictionary, Where the itterrows gives the index and row data 

nano_data_dict = {row.letter:row.code for (index,row)in nato_data.iterrows()}


print(nano_data_dict)

proxy1 = [nano_data_dict[l] for l in letters]

print(proxy1)