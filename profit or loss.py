actual_amount = float(input("Give the actual amount"))
sales_amount = float(input("Give the sales amount"))
if sales_amount > actual_amount : 
    amount = sales_amount - actual_amount
    print("Total profit is",amount)
else :
    print("No profit")