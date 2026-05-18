#writing to a file 

#with open("notes.txt", "w") as file :
#    file.write("this is your first note!\n")
#    file.write("you are handling file handling in python")

#read from a file 

with open ("notes.txt", "r") as false:
    content = file.read()
    print('file content:\n' , content)

#appending in file 
with open("notes.txt", "a") as false:
    file.write("\n this is an appended note")