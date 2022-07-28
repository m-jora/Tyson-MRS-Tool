from MRS_Ownership import Force_Ownership
from MRS_Ownership import main as Ownership_Main
from MRS_Withdraw import Withdraw_requests
from MRS_Withdraw import main as Withdraw_Main
import os, time

#import MRS_Withdraw.py as Withdraw
value = ''
valid = ['1', '2', '3']
clear = lambda: os.system('cls')

while value != '3':
    print('#############################################')
    print('##              MRS Tool Menu              ##')
    print('#############################################\n')

    print('Please Select Option:')
    print('1. Force Ownership of MRS Requests')
    print('2. Withdraw MRS Requests')
    print('3. Exit Program\n')

    value = str(input('Input Selection: '))
    if value not in valid:
        clear()
        print('Please Input a valid Selection\n')

    elif value == '1':
        clear()
        print('Please Select Option:')
        print('1. Train')
        print('2. Test')
        print('3. Dev')
        print('4. Sandbox')
        print('5. Prod\n')

        options = ['1', '2', '3', '4', '5']
        possible = False
        while not possible:
            choice = str(input('Input Selection: '))
            if choice in options:
                possible = True
            else:
                print('Please Input a valid Selection\n')

        clear()

        print('#############################################')
        print('##            MRS Ownership Tool           ##')
        print('#############################################\n')
        Ownership_Main(choice)

    elif value == '2':
        clear()
        print('Please Select Option:')
        print('1. Train')
        print('2. Test')
        print('3. Dev')
        print('4. Sandbox')
        print('5. Prod\n')

        options = ['1', '2', '3', '4', '5']
        possible = False
        while not possible:
            choice = str(input('Input Selection: '))
            if choice in options:
                possible = True
            else:
                print('Please Input a valid Selection\n')

        clear()
        
        print('#############################################')
        print('##            MRS Withdraw Tool            ##')
        print('#############################################\n')
        Withdraw_Main(choice)
        print('All Error IDs have been output to Error_IDs.xlsx\n')

    elif value == '3':
        print('Have a Nice Day')
        time.sleep(3)
