user_input = input("Enter a number: ")


try:
    number = float(user_input)  
    if '.' in user_input:  
        print("The entered number is a decimal.")
    else:
        print("The entered number is an integer.")
except ValueError:
    print("The entered value is not a valid number.")