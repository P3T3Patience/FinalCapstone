import math
'''Capstone Project
Print required statements.
Request input from user. 
change case to lower to prevent misinterpretation.
filter non relevant data with If statement'''
#Get user input: bond or investment
print("investment   - to calculate the amount of interest you'll earn on your investment")
print("bond         - to calculate the amount you'll have to pay on a home loan")
print()
user_entry = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")
#Make user input all lowercase to avoid issues
user_entry = user_entry.lower()
#If bond is selected, gather required information and calculate repayment per month
if user_entry == "bond":
    house_value = float(input("Please enter the present value of the house: £"))
    interest_rate = float(input("Please enter the interest rate (numbers only): "))
    repay_length = float(input("How many months do you plan to repay the bond in: "))
    interest_rate = (interest_rate / 100) / 12
    amount = (interest_rate * house_value) / (1 -(1 + interest_rate)**(-repay_length))
    print("Repayment per month: £" + str(round(amount, 2)))
#If investment is selected, gather required information and calculate the interest based on the selected type
elif user_entry == "investment":
    deposit = float(input("Please enter the amount you are depositing: £"))
    interest_rate = float(input("Please enter the interest rate (numbers only): "))
    invest_length = float(input("How many years do you plan on investing?: "))
    interest_type = str(input("Do you want 'simple' or 'compound' interest?: "))
    interest_type = interest_type.lower()
    interest_rate = interest_rate / 100
    if interest_type == "simple":
        print("Simple Interest with £" + str(deposit) + " for " + str(invest_length) + " years")
        amount = deposit * (1 + interest_rate * invest_length)
        print("Amount with interest: £" + str(round(amount, 2)))
    elif interest_type == "compound":
        print("Compound Interest with £" + str(deposit) + " for " + str(invest_length) + " years")
        amount = deposit * math.pow((1 + interest_rate), invest_length)
        print("Amount with interest: £" + str(round(amount, 2)))
#Error if neither bond or investment is entered
else:
    print("Error! Please type either 'bond' or 'investment'.")