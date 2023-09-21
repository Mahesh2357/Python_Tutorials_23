# code - 1
# list1 = []
# num = int(input("Enter number of elements in list: "))

# for i in range(1, num + 1):
#     ele = int(input("Enter elements: "))
#     list1.append(ele)

# print("Largest element is:", max(list1))

#! =====================================
from re import A


class Temperature():
    def __init__(self, celsius):
        if celsius > -273.15:
            self.celsius = celsius
        else:
            raise ValueError(
                'ERROR: Temperatures below -273C are not possible')


#! =====================================
class Account:
    def __init__(self):
        self.total_amt = 0

    def welcome(self):
        self.name = input(
            'Welcome to your Account... ')

    def current_bal(self):
        print('Your Current balance : ', self.total_amt)


    def credit(self):
        amt_to_credit = float(input('Enter amount to credit : '))

        if amt_to_credit < self.total_amt:
            print('Please credit the amount...')
        else:
            self.total_amt += amt_to_credit
        self.current_bal()


    def debit(self):
        amt_to_debit = float(input('Enter amount to debit : '))

        if amt_to_debit > self.total_amt:
            print('minimum Balance...')
        else:
            self.total_amt -= amt_to_debit
        self.current_bal()

class display_bal(Account):
    def __init__(self, account):
        super(display_bal, self).__init__
        print('Account balance : ', account.balance)
o1 = display_bal()


if __name__ == "__main__":
    Account = Account()
    Account.welcome()

    while True:
        int_val = int(
            input('Enter 1 : Display balance,\n2 : credit\n3 : debit\n'))

        if int_val == 1:
            Account.current_bal()
        elif int_val == 2:
            Account.credit()
        elif int_val == 3:
            Account.debit()
        else:
            print('Invalid input...')

o1.display_bal()
# print(o1)