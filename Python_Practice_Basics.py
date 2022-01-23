
#The first part is only practice wiht operational characters
# print("Hello World!")   
# type(3)

# a=8+22*2-4
# print(a)

# b=5+(9*3/(2-4))
# print(b)

#Creating a list an print by indexing, remember that the index start in 0
counties=['Araphoe','Denver','Jefferson']
print(counties[1])

#Negative indexes are used to identify a list item's position relative to the end of the list.
#To find the last item in the counties list, we would enter the following:
print(counties[-1])

#Find the lengh of a list using len() method
print(len(counties))

#Slice list are used to get a certain information inside a lsit, the first number is the index to start and the second number
#mark the end of the slice
print(counties[0:2])

#Alternatively we can use this slice too, if we do not specified the start index or the item number, python interpreter that is the start
#or the start number
print(counties[:2])
print(counties[0:])

#To add items to a list we use the append() method, this method add the new item to the end of the list
counties.append('El Paso')
print(counties)

#To add items to a list and specify where in a list we use the insert() method
#the first number represent the index number and the second the objet what we want to insert
counties.insert(2,'El Paso')
print(counties)

#To remove a item we use the remove() method
#Only remove the first item that found
counties.remove('El Paso')
print(counties)

#Another method we can use is the pop() method, we only need to specified the index number
counties.pop(-1)
print(counties)

#To change an item in a list, use the syntax list[index] on the left side of the equals sign; 
# on the right side, you assign the index a new data value
counties[2]='El Paso'
print(counties)

#Excercise
counties.insert(1,"El Paso")
counties.remove("Araphoe")
counties[1]='Jefferson'
counties[2]='Denver'
counties.append('Araphoe')
print(counties)





#Tuples are similar to lists in Python, with a major exception: once you create a tuple, it cannot be changed. 
#we use parentheses () instead of brackets []
counties_tuple=('Araphoe','Denver','Jefferson')
print(counties_tuple)


#A Python dictionary has a key and a value, or key-value pairs
#We use curly braces {} to enclosed the data in a dictionary
#The next line creates an empty dictionary
counties_dict={}

#To add keys and key-values we use the next line, the need to be inside brackets and in double quotes
counties_dict["Araphoe"]=422829
print(counties_dict)

#Add the rest of the lines
counties_dict["Denver"]=463353
counties_dict["Jefferson"]=432438
print(counties_dict)

#Getting the len of a dictionary
print(len(counties_dict))

#to get all the keys inside a dictionary we use the print() metho or the items() method
print(counties_dict.items())

#to get the keys we use the keys() method
print(counties_dict.keys())

#to get the values we use the values() method
print(counties_dict.values())

#to get the values of an specified key we can use the get() method
print(counties_dict.get('Denver'))
print(counties_dict['Araphoe'])

#We can get list of dictionaries too
voting_data=[]

#we can append the dictionaries one by one
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})

print(voting_data)

#Excercise
voting_data.insert(1,{"county":"El Paso","registered_voters":461149})
voting_data.pop(0)
voting_data[2]={"county":"Denver", "registered_voters": 463353}
voting_data[1]={"county":"Jefferson", "registered_voters": 432438}
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
print(voting_data)


import datetime as dt

now=dt.datetime.now()

print(f"The time right now is {now}")