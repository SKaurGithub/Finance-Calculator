import math

# Creating print statements to explain the two calculator options
# (investment calculator and home loan repayment calculator)
# and creating an input statement so the user can choose,
# which calculator they would like to use.

print("investment - to calculate the amount of interest"
      " you'll earn on your investment")
print("bond - to calculate the amount you'll have to pay "
      "on a home loan \n")   # \n is for readability

calculator_option = input("Enter either 'investment' or 'bond' "
                          "from the menu above to proceed: ")

# Creating if-elif-else statement + nested if statement in a while loop.
# Depending on, what the user will enter (investment/bond),
# the appropriate questions will be asked; inputs will be stored in variables,
# which will be used after to calculate the result.

start = True
while start:

    if calculator_option.lower() == "investment":

        deposit = input("Please enter the amount of money "
                        "that you are depositing: £")
        deposit.isdecimal()

        # Code below will only execute if user enters a non-numeric value.
        if not deposit.isdecimal():
            while True:
                deposit = input("Invalid, please enter a numeric value. "
                                "Please enter the amount of money "
                                "that you are depositing: £")
                deposit.isdecimal()
                if deposit.isdecimal():
                    break

        deposit = float(deposit)


        interest_rate = input("Please enter the interest rate "
                              "(as a percentage) "
                              "without the percentage sign '%': ")
        interest_rate.isdecimal()

        # Code below will only execute if user enters a non-numeric value.
        if not interest_rate.isdecimal():
            while True:
                interest_rate = input("Invalid, please enter a numeric value. "
                                      "Please enter the interest rate "
                                      "(as a percentage) "
                                      "without the percentage sign '%': ")
                interest_rate.isdecimal()
                if interest_rate.isdecimal():
                    break

        interest_rate = float(interest_rate)


        years = input("Please enter the number of years "
                      "you plan on investing: ")
        years.isdecimal()

        # Code below will only execute if user enters a non-numeric value.
        if not years.isdecimal():
            while True:
                years = input("Invalid, please enter a numeric value. "
                              "Please enter the number of years "
                              "you plan on investing: ")
                years.isdecimal()
                if years.isdecimal():
                    break

        years = float(years)


        interest = input("Please enter if you either want "
                         "'simple' or 'compound' interest: ")

        end = True
        while end:

            if interest.lower() == "simple":
                interest_rate_decimal = interest_rate / 100
                simple_result = deposit * (1 + interest_rate_decimal * years)
                rounded_result = round(simple_result, 2)
                print(f'The total amount once the interest of '
                      f'{interest_rate}% has been applied '
                      f'after the given period of {years} years '
                      f'is £{rounded_result}.')
                start = False
                break

            elif interest.lower() == "compound":
                interest_rate_deci = interest_rate / 100
                compound_result = deposit * math.pow\
                    ((1 + interest_rate_deci), years)
                rounded_result_com = round(compound_result, 2)
                print(f'The total amount once the interest of '
                      f'{interest_rate}% has been applied '
                      f'after the given period of {years} '
                      f'years is £{rounded_result_com}.')
                start = False
                break

            else:
                interest = input("Invalid entry. Please enter if you "
                                 "either want 'simple' or "
                                 "'compound' interest: ")


    elif calculator_option.lower() == "bond":
        value = input("Please enter the present value of the house: £")

        value.isdecimal()

        # Code below will only execute if user enters a non-numeric value.
        if not value.isdecimal():
            while True:
                value = input("Invalid, please enter a numeric value."
                              "Please enter the present value of the house: £")
                value.isdecimal()
                if value.isdecimal():
                    break

        value = float(value)


        interest_rate = input("Please enter the interest rate "
                              "(as a percentage) without "
                              "the percentage sign %: ")

        interest_rate.isdecimal()

        # Code below will only execute if user enters a non-numeric value.
        if not interest_rate.isdecimal():
            while True:
                interest_rate = input("Invalid, please enter a numeric value. "
                                      "Please enter the interest rate "
                                      "(as a percentage) without "
                                      "the percentage sign %: ")
                interest_rate.isdecimal()
                if interest_rate.isdecimal():
                    break

        interest_rate = float(interest_rate)


        months = input("Please enter the number of months "
                       "you plan to take to repay the bond: ")

        months.isdecimal()

        # Code below will only execute if user enters a non-numeric value.
        if not months.isdecimal():
            while True:
                months = input("Invalid, please enter a numeric value. "
                               "Please enter the number of months "
                               "you plan to take to repay the bond: ")
                months.isdecimal()
                if months.isdecimal():
                    break

        months = float(months)


        monthly_interest_rate = interest_rate / 100 / 12
        repayment = (monthly_interest_rate * value)\
                    /(1 - (1 + monthly_interest_rate) ** (-months))
        rounded_repayment = round(repayment, 2)
        print(f'The monthly repayment would be £{rounded_repayment}')
        break

    else:
        calculator_option = input("Unfortunately, your entry was invalid. "
                                  "Please enter either 'investment' "
                                  "or 'bond' to proceed: ")
