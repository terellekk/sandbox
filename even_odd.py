#Function checks if a number is even or odd

def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

check_number_output = even_or_odd(1)
print(check_number_output)