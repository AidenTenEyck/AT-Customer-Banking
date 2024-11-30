# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from cd_account import create_cd_account
from savings_account import create_savings_account
# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    '''
    float_check acts as revolving True/False variable
    Functions operate with simple interest formula
    '''
    # ADD YOUR CODE HERE
    #User input for Savings Account
    float_check=False
    while float_check==False:
        savings_balance=input(f'What is the balance of your Savings Account?: ')
        try:
            float(savings_balance)
            float_check=True
        except ValueError:
            print('Please enter numberical value!')
    savings_balance=float(savings_balance)
    while float_check==True:
        savings_interest=input(f'What is the interest rate of your Savings Account?: ')
        try:
            float(savings_interest)
            float_check=False
        except ValueError:
            print('Please enter numerical value!')
    savings_interest=float(savings_interest)
    while float_check==False:
        savings_months=input(f'How many months has your Savings Account collected interest?: ')
        if savings_months.isdigit():
            savings_months=int(savings_months)
            float_check=True
        else:
            print('Please enter whole month value')

    # Call the create_savings_account function and pass the variables from the user.
    savings_account=create_savings_account(savings_balance,savings_interest,savings_months)
    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f'Savings Account:\n Interest Earned: ${round(savings_account.interest,2)} - New Balance: ${round(savings_account.balance,2)}')
    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    #User input for CD account
    while float_check==True:
        cd_balance=input(f'What is the balance of your CD Account?: ')
        try:
            float(cd_balance)
            float_check=False
        except ValueError:
            print('Please enter numberical value!')
    cd_balance=float(cd_balance)
    while float_check==False:
        cd_interest=input(f'What is the interest rate of your CD Account?: ')
        try:
            float(cd_interest)
            float_check=True
        except ValueError:
            print('Please enter numerical value!')
    cd_interest=float(cd_interest)
    while float_check==True:
        cd_months=input(f'How many months has your CD Account collected interest?: ')
        if cd_months.isdigit():
            cd_months=int(cd_months)
            float_check=False
        else:
            print('Please enter whole month value')
    # Call the create_savings_account function and pass the variables from the user.
    cd_account=create_cd_account(cd_balance,cd_interest,cd_months)
    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f'CD Account:\n Interest Earned: ${round(cd_account.interest,2)} - New Balance: ${round(cd_account.balance,2)}')
    # Call the main function.
if __name__ == "__main__":
    main()