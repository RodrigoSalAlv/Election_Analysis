#Decision Statements

# How many votes did you get?
my_votes = int(input("How many votes did you get in the election? "))
#  Total votes in the election
total_votes = int(input("What is the total votes in the election? "))
# Calculate the percentage of votes you received.
percentage_votes = (my_votes / total_votes) * 100
# print("I received " + str(percentage_votes)+"% of the total votes.")
#this is the f-print format, you dont need to cast the variables to get print the information
print(f"I received {my_votes/total_votes*100}% of the total votes.")

#Ifstatems
#This is a regular if statement, if the condition is true, the statement happen
counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])


#This is an if-else statement, if the condition is true: the firs statemen happen, if the condition is false the else statement happen
#we cast the input into a integrer to python undestand its a number
temperature = int(input("What is the temperature outside? "))

if temperature > 80:
    print("Turn on the AC.")
else:
    print("Open the windows.")



#This is an if-else nested statement, multiple conditions happen in case the main statement is False
#this could be a little complex due to the quantity of conditions, and could be a little hard to read

#What is the score?
score = int(input("What is your test score? "))

# Determine the grade.
if score >= 90:
    print('Your grade is an A.')
else:
    if score >= 80:
        print('Your grade is a B.')
    else:
        if score >= 70:
            print('Your grade is a C.')
        else:
            if score >= 60:
                print('Your grade is a D.')
            else:
                print('Your grade is an F.')


#The if-elif-else statement is the same than if-else nested statement, but easier to write and read:

# What is the score?
score = int(input("What is your test score? "))

# Determine the grade.
if score >= 90:
    print('Your grade is an A.')
elif score >= 80:
    print('Your grade is a B.')
elif score >= 70:
    print('Your grade is a C.')
elif score >= 60:
    print('Your grade is a D.')
else:
    print('Your grade is an F.')


#Membership operators are used to test if an object,
#like a string, integer, or other data type is present in an expression, list, tuple, or dictionary.

counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")


# Logical operators allow us to connect multiple comparison expressions to create a compound expression
#Logical AND
if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")


#Logical OR
if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties.")


#Logical NOT
if "Arapahoe" in counties and "El Paso" not in counties:
       print("Only Arapahoe is in the list of counties.")
else:
    print("Arapahoe is in the list of counties and El Paso is not in the list of counties")


#F-Strings, print multiple lines on the screen using the f-format

candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate=(
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes/total_votes*100:.w2f}% of the total votes.")

print(message_to_candidate)