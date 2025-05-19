#there is concept of nesting the list and dictionaries within the same



nested_list = ["A","B",["C","D"]]


#Where we can access the nestede list item as a array element as well 


print(nested_list[2][0])
print(nested_list[2][1])

#same as this concept consider a dictionary with list as Value for a key


student_details = {
    "name" : ["arjun","ajith","balu","diwakar","sunny"],
    "age" : [11,12,13,10,14]
    
    }



#the above details can be accessed by moreover the same concept as above

print(student_details["name"][0])
print(student_details["age"][0])

# we can even find the length of the list 

length = len(student_details["name"])

print(length)

#looping through the items
for items in student_details["name"] :
    print(items)

#consider having a nested dictionary


travel_log = {
    "France" :{
        "cities" : ["Paris","san Deiago","Rome"],
        "month" : "Feb"
    
    },
    "America" : {
        "cities" : ["New York","Washington","San andreas"],
        "month" : "Mar"
    }
}


#LETS SEE HOW WE CAN ACCESS THE PLACES INSIDE THE DICTIONARIES BASED ON INPUT


KEY = input("Please enter the country to get the details : ")

for cities in travel_log[KEY]["cities"]:
    print(cities)
    print(travel_log[KEY]["month"])


