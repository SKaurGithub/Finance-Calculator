import math

# Creating print statements to explain the two calculator options (investment calculator and
# home loan repayment calculator) and creating an input statement so the user can choose,
# which calculator they would like to use.

print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond - to calculate the amount you'll have to pay on a home loan \n")   # \n is for readability

calculator_option = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")

# Creating if-elif-else statement + nested if statement. Depending on, what the user will enter (investment/bond),
# the appropriate questions will be asked; inputs will be stored in variables,
# which will be used after to calculate the result.

if calculator_option.lower() == "investment":
    deposit = float(input("Please enter the amount of money that you are depositing: "))
    interest_rate = float(input("Please enter the interest rate (as a percentage) without the percentage sign '%': "))
    years = float(input("Please enter the number of years you plan on investing: "))
    interest = input("Please enter if you either want 'simple' or 'compound' interest: ")

    if interest.lower() == "simple":
        interest_rate_decimal = interest_rate / 100
        simple_result = deposit * (1 + interest_rate_decimal * years)
        print(f'The total amount once the interest of {interest_rate}% has been applied \n'
              f'after the given period of {years} years is {simple_result}.')

    elif interest.lower() == "compound":
        interest_rate_decimal = interest_rate / 100
        compound_result = deposit * math.pow((1 + interest_rate_decimal), years)
        print(f'The total amount once the interest of {interest_rate}% has been applied \n'
              f' after the given period of {years} years is {compound_result}.')

    # This statement below will ask the user to enter the input (simple/compound) again if previous input was invalid.
    # I know that after entering the correct input the program will end.
    # I am working on improving this.

    else:
        interest = input("Invalid entry. Please enter if you either want 'simple' or 'compound' interest: ")


elif calculator_option.lower() == "bond":
    value = float(input("Please enter the present value of the house: "))
    interest_rate = float(input("Please enter the interest rate (as a percentage) without the percentage sign %: "))
    months = float(input("Please enter the number of months you plan to take to repay the bond: "))

    monthly_interest_rate = interest_rate / 100 / 12
    repayment = (monthly_interest_rate * value)/(1 - (1 + monthly_interest_rate) ** (-months))
    print(f'The monthly repayment would be {repayment}')

# As described previously, after entering the correct input below the program will end.
# I am working on improving this.

else:
    calculator_option = input("Unfortunately, your entry was invalid.\n"
                              "Please enter either 'investment' or 'bond' to proceed: ")
