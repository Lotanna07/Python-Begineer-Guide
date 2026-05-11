#the while loop

#while conditions:
    #repetative code  


count = 1
while count <= 5:
    print("count is ", count)
    count += 1



# the for loop
#for i range(start, stop, step):

#   #repeat this blocks

#range(1,6) that means start from 1 and step before 6 => (1, 2, 3, 4, 5)

for i in range(1, 6):
    print("Number: ", i)


#loop through a list 
fruits = ("apple", "banana", "cherry")
for fruit in fruits:
    print(fruit.capitalize())