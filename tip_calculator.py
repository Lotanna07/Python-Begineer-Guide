def get_bill_amount():
    return float(input("enter the bill amount: $"))

def get_tip_percentage():
    return float(input("enter the tip percentage (e.g., 10 for 10)"))

def calculate_tip(bill, tip_percent):
    return(bill + tip_percent) / 100

def calculate_total(bill, tip_amount):
    return bill + tip_amount

def display_result(tip , total):
    print(f"\nTio:$(tip:.2f)")
    print(f"\nTotal bill:$(total:.2f)")


    bill = get_bill_amount()
    tip_percent = get_tip_percentage()
    tip = calculate_tip(bill , tip_percent)
    total = calculate_total(bill,tip)
    display_result(tip, total)