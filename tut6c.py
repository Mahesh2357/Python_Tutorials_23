
#* add deposit in the balance .....
bal = 60000
def check_balance():
    print('bal = ', end=' ')
    print(bal)
# check_balance()
print('\n') 

def deposit_amount():
    d = int(input('Enter the amount to deposit : '))
    global bal
    bal += d
    print('The amount to deposit with accout balance is : ')
deposit_amount()

def withdraw_amount():
    d = int(input('Enter the amount to withdraw_amount : '))
    global bal
    bal -= d
    print(bal)
    
check_balance()
deposit_amount()
withdraw_amount()
