#create a dictionary

student = [] #list


student ={
    "name" : "Alice",
    "age" : 20,
    "grade" : "A"

}

print(student.keys())
print(student.values())
print(student.get("name"))

#accessing and modifying values 

#print(student["age"])
#print(student("grade"))
#print(student.get("grade"))


#student["age"] = 21
#student ["major"] ="math"

#print(student)

#loop through a dictionary
for key, value in student.item():
    print(f"{key} : {value}")