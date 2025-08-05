def calculate_bill():
    print("Welcome to the Bill Splitter App!")

    total_bill = float(input("Enter total bill amount: "))
    people = int(input("Enter number of people: "))
    tip_percentage = int(input("Enter tip percentage (0/5/10/15/20): "))

    if tip_percentage == 0:
        tip = 0
    elif tip_percentage == 5:
        tip = total_bill * 0.05
    elif tip_percentage == 10:
        tip = total_bill * 0.10
    elif tip_percentage == 15:
        tip = total_bill * 0.15
    elif tip_percentage == 20:
        tip = total_bill * 0.20
    else:
        print("Invalid tip percentage! Setting tip to 0.")
        tip = 0

    total_with_tip = total_bill + tip
    per_person = total_with_tip / people

    print("\nTip Amount: ₹{:.2f}".format(tip))
    print("Total Bill (with Tip): ₹{:.2f}".format(total_with_tip))
    print("Each person should pay: ₹{:.2f}".format(per_person))

calculate_bill()