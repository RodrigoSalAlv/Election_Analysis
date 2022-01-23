#This is just the first line I will write for my entire life
print("Esta es la primer linea que escribirás para el resto de tu vida")

x = 1
y = 10

# equal to condition
if x == 2:
    print ("X is equal to 1")
else:
    print ("x not equal to 1")

#Greater than
if x > 1:
    print("X IS GREATER THAN x")
else:
    print("X is not greater than 1")

#Nested conditions
if x < 10:
    if y<5:
        print("x is less than 10 and y is less than 5")
    elif y == 5:
        print ("x is less than 10 and y is equal to 5")
    else:
        print("x is less than 10 and y is greter than 5")
else:
    print ("x is greater than 10")



#index with an ending number
for y in range(50):
    print(y)

#index startin and ending in such number
for x in range (2, 10):
    print(x)


run = 'y'

while run=='y':
    print ("Hi!")
    run = input("To run again. Enter 'y'")
