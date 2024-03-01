from functools import reduce

def multiply_numbers_in_list(numbers):
    result = reduce(lambda x, y: x * y, numbers)
    return result

# Example usage:
numbers_list = [2, 3, 4, 5]
result = multiply_numbers_in_list(numbers_list)
print(f"Multiplication result: {result}")





def count_upper_lower_case(string):
    upper_count = sum(1 for char in string if char.isupper())
    lower_count = sum(1 for char in string if char.islower())
    return upper_count, lower_count

# Example usage:
input_string = "Hello World"
upper, lower = count_upper_lower_case(input_string)
print(f"Uppercase count: {upper}, Lowercase count: {lower}")




def is_palindrome(string):
    reversed_string = string[::-1]
    return string.lower() == reversed_string.lower()

# Example usage:
input_str = "Racecar"
if is_palindrome(input_str):
    print(f"{input_str} is a palindrome.")
else:
    print(f"{input_str} is not a palindrome.")





import time
from math import sqrt

def square_root_after_delay(number, milliseconds):
    time.sleep(milliseconds / 1000)
    result = sqrt(number)
    print(f"Square root of {number} after {milliseconds} milliseconds is {result}")

# Example usage:
square_root_after_delay(25100, 2123)



def all_elements_true(input_tuple):
    return all(input_tuple)

# Example usage:
bool_tuple = (True, True, True)
result = all_elements_true(bool_tuple)
print(f"All elements are true: {result}")
