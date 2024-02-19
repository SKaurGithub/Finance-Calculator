import math


def separator(length=80, symbol="-"):
    """
    This function creates a separator which helps with readability.
    """
    print(length * symbol)


def is_decimal(prompt):
    """
    This function will check if the input is numeric -
    if so, it will be cast into a float otherwise
    the user will be prompt to enter a numeric value.
    :param prompt: different questions being asked to the user
    :return: return each input value
    """
    while True:
        input_value = input(prompt)
        if input_value.isdecimal():
            input_value = float(input_value)
            return input_value
        else:
            while True:
                input_value = input("Invalid, please enter "
                                    "a numeric value. " + prompt)
                if input_value.isdecimal():
                    input_value = float(input_value)
                    return input_value


# Creating print statements to explain the two calculator options
# (investment calculator and home loan repayment calculator)
# and creating an input statement so the user can choose,
# which calculator they would like to use.

print("\n***** Welcome to the Finance Calculator *****\n")
separator()

rerun = True
while rerun:

    print("investment - to calculate the amount of interest"
          " you'll earn on your investment")
    print("bond - to calculate the amount you'll have to pay "
          "on a home loan \n")   # \n is for readability

    calculator_option = input("Enter either 'investment' or 'bond' "
                              "from the menu above to proceed: ")

    # Creating if-elif-else statement + nested if statement in a while loop.
    # Depending on, what the user will enter (investment/bond),
    # the appropriate questions will be asked;
    # inputs will be stored in variables,
    # which will be used after to calculate the result.

    start = True
    while start:

        if calculator_option.lower() == "investment":

            deposit = is_decimal("Please enter the amount of money "
                                 "that you are depositing: £")

            interest_rate = is_decimal("Please enter the interest rate "
                                       "(as a percentage) "
                                       "without the percentage sign '%': ")

            years = is_decimal("Please enter the number of years "
                               "you plan on investing: ")

            interest = input("Please enter if you either want "
                             "'simple' or 'compound' interest: ")


            end = True
            while end:

                if interest.lower() == "simple":
                    interest_rate_decimal = interest_rate / 100
                    simple_result = deposit * \
                                    (1 + interest_rate_decimal * years)
                    rounded_result = round(simple_result, 2)
                    separator()
                    print(f'The total amount once the interest of '
                          f'{interest_rate}% has been applied\n'
                          f'after the given period of {years} years '
                          f'is £{rounded_result}.')
                    separator()
                    start = False
                    break


                elif interest.lower() == "compound":
                    interest_rate_deci = interest_rate / 100
                    compound_result = deposit * math.pow\
                        ((1 + interest_rate_deci), years)
                    rounded_result_com = round(compound_result, 2)
                    separator()
                    print(f'The total amount once the interest of '
                          f'{interest_rate}% has been applied\n'
                          f'after the given period of {years} '
                          f'years is £{rounded_result_com}.')
                    separator()
                    start = False
                    break


                else:
                    interest = input("Invalid entry. Please enter if you "
                                     "either want 'simple' or "
                                     "'compound' interest: ")


        elif calculator_option.lower() == "bond":
            value = is_decimal("Please enter the present "
                               "value of the house: £")

            interest_rate = is_decimal("Please enter the interest rate "
                                       "(as a percentage) without "
                                       "the percentage sign %: ")

            months = is_decimal("Please enter the number of months "
                                "you plan to take to repay the bond: ")

            monthly_interest_rate = interest_rate / 100 / 12
            repayment = (monthly_interest_rate * value)\
                        /(1 - (1 + monthly_interest_rate) ** (-months))
            rounded_repayment = round(repayment, 2)
            separator()
            print(f'The monthly repayment would be £{rounded_repayment}')
            separator()
            break


        else:
            calculator_option = input("Unfortunately, your entry was invalid."
                                      " Please enter either 'investment' "
                                      "or 'bond' to proceed: ")


    # Allow user to reuse the calculator or exit.
    if input("\nPress \"Enter\" to do another finance calculation "
             "or type anything to quit:\n"):
        print("\nThank you for using Finance Calculator!\n"
              "See you soon!")
        start = False
        rerun = False
    else:
        separator()
