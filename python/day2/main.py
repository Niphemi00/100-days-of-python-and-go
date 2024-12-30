print("Welcome to the tip calculator")
bill_amount = float(input("What was the total bill? $"))
tip_amount = float(input("How much tip (in percentage of bill) would you like to give 10, 12, or 15? "))
tip_amount = (tip_amount / 100) * bill_amount
bill_amount += tip_amount
payers_quantity = int(input("How many people are to split the bill? "))
payers_share = bill_amount / payers_quantity
print("Each person should pay: $", round(payers_share, 2))