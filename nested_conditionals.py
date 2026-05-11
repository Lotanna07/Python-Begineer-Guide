#nested conditionals

age = 25
has_ticket = True 

if age >= 18:
    if has_ticket:
        print("welcome to the concert")
    else:
        print("you need a ticket ")
else:
    print("your too young ")