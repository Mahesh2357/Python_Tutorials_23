
#* add deposit in the balance .....
bal = 60000
def check_balance():
    print('bal = ', end=' ')
    print(bal)
check_balance()
print('\n') 

def deposit_amount():
    d = int(input('Enter the amount to deposit : '))
    t = d + bal
    print('The amount to deposit with accout balance is : ',+ t, end=' ')
deposit_amount()
