print('Welcome to the calculator')
print('Enter characters without spaces, use arithmetic characters + - * /')
print()
print('Write "Exit" to exit the program')
print()

while True:
    n = input()
    if n == 'Exit':  # Condition for exiting the program
        print('Calculator is stopped. Goodbye')
        break
    if n.count(' ') > 0:  # Condition for further use of the split() method
        print('Please, enter characters without spaces')
    else:
        if '+' in n:
            try:  # try/except block to detect an input error str instead of int
                num1, num2 = map(int, n.split('+'))  # map function to create an array with two numbers
            except ValueError:
                print('You must enter 2 numbers and 1 arithmetic sign')
            else:
                print(num1 + num2)
        elif '-' in n:
            try:
                num1, num2 = map(int, n.split('-'))
            except ValueError:
                print('You must enter 2 numbers and 1 arithmetic sign')
            else:
                print(num1 - num2)
        elif '*' in n:
            try:
                num1, num2 = map(int, n.split('*'))
            except ValueError:
                print('You must enter 2 numbers and 1 arithmetic sign')
            else:
                print(num1 * num2)
        elif '/' in n:
            try:
                num1, num2 = map(int, n.split('/'))
            except ValueError:
                print('You must enter 2 numbers and 1 arithmetic sign')
            except ZeroDivisionError:  # try/except block to detect ZeroDivisionError
                print("You can't divide by zero")
            else:
                print(num1 / num2)
        else:
            print('Please, use arithmetic characters + - * /')
