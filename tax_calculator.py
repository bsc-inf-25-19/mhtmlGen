income = float(input("Enter the annual income: "))

#
# Write your code here.
#
tax = 0
if income<=85_528:
    tax = 0.18*income - 556
elif income>85_528:
    tax = 0.32 * (income - 85_528) + 14_839
    
if tax < 0 :
    tax = 0
tax = round(tax, 0)
print("The tax is:", tax, "thalers")
