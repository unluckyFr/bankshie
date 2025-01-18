# bank system project 4 cs
#SEEING IF COMMIT WORKS
import random as r

class BankAccount:
    def __init__(self, age, name, password, balance=0, withdrawl_limit=500):
        self.name = name
        self.age = age
        self.balance = balance
        self.password = password
        self.withdrawl_limit = withdrawl_limit

    def display(self):
        print(f'Account name: {self.name}\n'
              f'Age: {self.age}'
              f'Balance: {self.balance}'
              f'Withdrawl Limit: ${self.withdrawl_limit: .2f}')

    def deposit(self, ammount):
        if ammount > 0:
            self.balance += ammount
            print(f'${ammount: .2f} added to your account. Current balance: ${self.balance}')
        else:
            print('Input a number bigger than 0 please!')

    def withdrawl(self, ammount):
        if ammount <= self.balance and ammount < self.withdrawl_limit:
            self.balance -= ammount
            print(f'${ammount: .2f} withdrawn from your account. ${self.balance: .2f} left in account.')
            self.withdrawl_limit -= ammount
            print(f'${self.withdrawl_limit: .2f} can be withdrawn today, until limit is reached.')
        else:
            print('Insufficient funds.')

    def transfer(self, other, ammount):
        if ammount <= self.balance:
            self.balance -= ammount
            other.balance += ammount
            print(f'${ammount: .2f} transferred from your account to . ${self.balance: .2f} left in account.')
        else:
            print('Insufficient funds.')

    def update_acc(self, new_name, new_age, new_withdrawl_limit, new_pass):
        self.name = new_name
        self.age = new_age
        self.withdrawl_limit = new_withdrawl_limit
        self.password  = new_pass
        print(f'Account details updated, name: {self.name}, age: {self.age}, withdrawl limit: {self.withdrawl_limit}, password: {new_pass}')

def pass_validate(word):  #validation function for the user passsword
    count= 0
    special_ca_set = '!@#$%^&*()_+-=`~:;/?.>,<{}[]'
    if len(word) > 8:
        count += 1
    else:
        print('Password needs to be longer than 8 characters.')
    if any(c in special_ca_set for c in word):
        count+=1
    else:
        print('Password has to include at least one special character.')
    if any(c.isupper() for c in word):
        count += 1
    else:
        print('Password has to include at least one capitalised letter.')
    if any(c.isdigit() for c in word):
        count += 1
    else:
        print('Password has to include at least one number.')
    if count == 4:
        return True
    else:
        return False

def random_password():  #instead of making a password, the user has the choice to generate one, in order to allways be inside the criteria, it takes 5 numbers, 5 capital letters, 5 special characters and 10 random ones and has a length of 25
    special_char = '!@#$%^&*()_+=-~`,./?<>[]{}|;:\'\"\\'
    characters = [chr(i) for i in range(33, 127)]  #all printable ascii characters
    nums = '1234567890'
    capital = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    capital = (r.choices(capital, k=5))  #5 capital letters e.g QHJRB
    num = (r.choices(nums, k=5))  #5 numbers
    special = (r.choices(special_char, k=5))  #5 special characters e.b: 19854
    password = (r.choices(characters, k=10))  #10 random printable ascii characters
    password += num + special + capital  #combine all of them together
    r.shuffle(password)  #shuffle them since when we combine them the list is in order (random characters, numbers, special character and then capital characters)
    password = ''.join(password)  #make the password a string
    return password



def main():
    accounts = {}

    while True:  # other things: offers/store; support for different currencies(stored in a mini account); shortcut for transfer(no need 4 id) etc
        print(f'\nWelcome! Select one option please:\n'
              f'1. Create an account\n'
              f'2. View account details\n'
              f'3. Edit account details\n'
              f'4. Deposit money into your account\n'
              f'5. Withdraw money from your account\n'
              f'6. Transfer money into another account\n'
              f'7. View all accounts (ADMINS) only\n'
              f'8. Our Store\n'
              f'10. Exit')

        try:
            choice = int(input('\nInput a number 1-10'))
        except TypeError:
            print('Please input a whole number ')

        match choice:

            case 1:  # make an account
                acc_id = str(len(accounts) + 1)
                name = input('Input your name:  ')
                age = int(input('Input your age:  '))
                while True:
                    c = input('\n1. To make a password\n2. To automatically generate one\n... ')
                    if c =='1':
                        password = input('Password criteria:\n'
                                         'Longer than 8 characters\n'
                                         'Has at least one special character\n'
                                         'Contains at least one capital letter\n'
                                         'Contains at least one number\n'
                                         'Input a password:  ')
                        if pass_validate(password):
                            print('Password accepted.')
                            break
                        else:
                            print('make a valid password.')
                    elif c == '2':
                        password = random_password()
                        break
                    else:
                        print('Input a valid option')
                accounts[acc_id] = BankAccount(age, name, password)
                print(
                    f'Account {acc_id} succsesfully created, name: {accounts[acc_id].name}| age: {accounts[acc_id].age}')
                with open('accounts.txt', 'a') as file:
                    file.write(f'  {acc_id}\n')

            case 2:  # view account details
                acc_id = input('Input your account id please!')
                if acc_id in accounts:
                    user_password = input('\nPlease input your password: ')
                    if user_password == accounts[acc_id].password:
                        print(f'Account id: {acc_id}\n'
                              f'Name: {accounts[acc_id].name}'
                              f'Age: {accounts[acc_id].age}'
                              f'Current Balance: {accounts[acc_id].balance}'
                              f'Withdrawal Limit: {accounts[acc_id].withdrawl_limit}')
                    else:
                        print('Wrong password try again!')
                else:
                    print('This account id does not exist, make sure to input the correct id or create an account now!')

            case 3:  # change account credentials
                acc_id = input('What is your account id?')
                if acc_id not in accounts:
                    print('This account doesnt exist!')
                else:
                    try:
                        while True:  # input and validate new name
                            new_name = str(input('What is you new name?'))
                            if any(n.isdigit() for n in new_name):
                                print('Can\'t have a name with digits')
                            else:
                                break

                    except TypeError:
                        print('Input a string please')

                    try:
                        while True:  # input and validate new age
                            new_age = int(input('Whats your age?'))
                            if not new_age >= 18:
                                print('Cant be smaller than 18')
                            else:
                                break
                    except TypeError:
                        print('Enter a whole number')
                    n = input('Do you want to change your withdrawl limit? y/n').strip().lower()
                    while True:
                        if n == 'y':
                            new_withdrawl_limit = int(input('Input your new withdrawl limit: '))
                            if new_withdrawl_limit > 1500:
                                print(
                                    'For values bigger than $1500 an official request is needed, you can write one from the menu!')
                                break
                        elif n == 'n':
                            break
                        else:
                            print('Enter a valid option')

                    accounts[acc_id].update_acc(new_age, new_age, new_withdrawl_limit)

            case 4:  # deposit money into an account
                acc_id = input('Enter your account id: ')
                if acc_id in accounts:
                    ammount = int(input('Input the ammount you would like to deposit into your account:   '))
                    accounts[acc_id].deposit(ammount)
                    print(f'New balance: {accounts[acc_id].balance: .2f}, ${ammount: .2f} deposited in the account!')
                else:
                    print('This account id does not exist, make sure to input the correct id or create an account now!')

            case 5:  # withdraw money
                acc_id = input('Enter your account id: ')
                if acc_id in accounts:
                    ammount = int(input('Input the ammount you would like to deposit into your account:   '))
                    if ammount <= accounts[acc_id].balance:
                        accounts[acc_id].deposit(ammount)
                        print(
                            f'New balance: {accounts[acc_id].balance: .2f}, ${ammount: .2f} withdrawn from the account!')
                    else:
                        print('Insufficient funds (ur brok)')
                else:
                    print('This account id does not exist, make sure to input the correct id or create an account now!')

            case 6:  # transfer money
                acc_id = input('Enter your account id: ')
                other_id = input('Enter the id for hte target account:  ')
                if acc_id in accounts:
                    if other_id in accounts:
                        ammount = int(input('Input the ammount you would like to deposit into your account:   '))
                        if ammount <= accounts[acc_id].balance:
                            accounts[acc_id].transfer(other_id, ammount)
                            print(
                                f'New balance: {accounts[acc_id].balance: .2f}, ${ammount: .2f} transferred from the account to account {other_id}!')
                        else:
                            print('Insufficient funds (ur brok)')
                    else:
                        print('Target account id does not exist!')
                else:
                    print('This account id does not exist, make sure to input the correct id or create an account now!')

            case 7:  # view all accounts
                if accounts:
                    for n in accounts.keys():
                        print(
                            f'Account id: {n}| Name: {accounts[n].name}| Age: {accounts[n].age}| Balance: {accounts[n].balance}| Withdrawl Limit: {accounts[n].withdrawl_limit}')
                else:
                    print('No accounts in database!')

            case 10:
                break

            case _:
                print('input a valid option')


if __name__ == '__main__':
    main()
