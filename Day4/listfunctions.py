fruits = ["Banana","Cherry","Mango"]

#append function to add things to last of list

fruits.append("apple")

print(fruits)

#extention can be used when mutiple things need to be appended so those can be kept another list and can be addded with extend

fruits2 = ["stawberry","pineapple","lichi"]
fruits.extend(fruits2)

print(len(fruits))

print(fruits)

#insert funxtion to insert items in specific index
fruits.insert(1,"promogranate")

print(fruits)


#pop function to remove last item

last_item = fruits.pop()

print(last_item)

print(fruits)

#remove function to remove specific items by value


fruits.remove("Mango")

print(fruits)


# sub array can be created by : , it will create a sub array from number1 to number2-1

subarr = fruits[0:2]

print(subarr)


