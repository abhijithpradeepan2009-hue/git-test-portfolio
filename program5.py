bill_amount = float(input("Enter the bill amount: "))
tip_percentage = float(input("Enter the tip percentage:"))
tip_amount = bill_amount * tip_percentage / 100
total_bill = bill_amount + tip_amount
print("Tip Amount:", tip_amount)
print("Total Bill:", total_bill)