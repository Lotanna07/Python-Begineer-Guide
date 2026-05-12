# defining a functions

#def functionName():
    # code block

#def greet():
#    print("hello, python developers!")

#greet()

#greet()


def greet(name):
    print(f"hello,{name}!")

greet("alice")
greet("manny")

#return value 
def addNumber(num1 , num2):
    return num1 + num2

result = addNumber(35 , 32)
print("sum is:", result)