#While Loops
# while loops test if a condition is true. If the condition is true, then the code will perform a task.

from itertools import count


x = 0
while x <= 5:
    print(x)
    x = x + 1


#For Loops
# for loops iterate, or run through, a program a specific number of times before it stops.

counties=['Araphoe','Denver','Jeffeson']

for county in counties:
    print(county)

#There is also a function calle range(), this function could be use in case we want to print just numbers and there is no
#need to write a list, just remember that the range() function start with the number '0'

for num in range(5):
    print(num)


#In case we need to run a for loop as many times as the lenght of a list, we can use the indexing functions together with
# the range() function

for i in range(len(counties)):
    print(i)



#We can use a for loop to iterate over a dictionary and get all the keys, all the values, or all the keys and value
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

#We can print the keys only by writing the name of the dictionary, just like a list
for county in counties_dict:
    print(county)

#Also if we want to specifiy we want the keys only, we can use the keys() function

for county in counties_dict.keys():
    print(county)

#If we want to see the values, we can use the values() function in the for loop
for voter in counties_dict.values():
    print(voter)

#Another wey to get the values we can use the format dictionary_name[key]
# remeber that if we put the key name inside de brackets, we will get the value of that key in the dictionary_name[key] format
for county in counties_dict:
    print(counties_dict[county])


#Also we can use the get() method, to get the values of a dictionary
# remember that using the get() method, we need to put into parenthesis the key name
for county in counties_dict:
    print(counties_dict.get(county))


#If we want to print the key-value pair of the dictionary, we use the items() method in the for loop
# remember that when we use the items() we get both the keys and the values
#  also remember that when iterating over a dictionary, the first varable is assinged to the keys and the second to the values.

for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters.")



#We can also iterate into a list of dictionaries 

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]


for county_dict in voting_data:
    print(county_dict)

#If we want to print the keys inside a list of dictionaries

for i in range(len(voting_data)):
    print(voting_data[i]['county'])


#To retrieve keys and values, separately from each dictionary in the list of dictionaries, we need to use a nested for loop
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)


#If we only want to print the county name from each dictionary, we can use county_dict['county'] in the print statement for the for loop.
for county_dict in voting_data:
    print(county_dict['county'])