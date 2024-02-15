# Functions

# Function to calculate factorial using recursion
def calculate_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * calculate_factorial(n-1)

# Function to reverse a string
def reverse_string(s):
    return s[::-1]

# Function to get the maximum of three numbers
def get_max(a, b, c):
    return max(a, b, c)

# Function to check if a number is even
def is_even(num):
    return num % 2 == 0

# Function to filter prime numbers from a list
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]

# Function to find common elements between two lists
def find_common_elements(list1, list2):
    return list(set(list1) & set(list2))

# Function to calculate word frequency in a string
def word_frequency(input_string):
    words = input_string.split()
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency

# Recursive function to calculate the nth Fibonacci number
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Function to calculate running average of a series of numbers
def calculate_running_average(numbers):
    running_sum = 0
    averages = []
    for i, num in enumerate(numbers, 1):
        running_sum += num
        averages.append(running_sum / i)
    return averages


# Classes and Objects

# Parent class My_shape
class My_shape:
    def __init__(self, color="default_color", is_filled=True):
        self.color = color
        self.is_filled = is_filled

    def __str__(self):
        return f"Color: {self.color}, Filled: {self.is_filled}"

    def getArea(self):
        return 0


# Child class Rectangle
class Rectangle(My_shape):
    def __init__(self, color="default_color", is_filled=True, x_top_left=0, y_top_left=0, length=1, width=1):
        super().__init__(color, is_filled)
        self.x_top_left = x_top_left
        self.y_top_left = y_top_left
        self.length = length
        self.width = width

    def __str__(self):
        return f"{super().__str__()}, Type: Rectangle, Top Left: ({self.x_top_left}, {self.y_top_left}), Length: {self.length}, Width: {self.width}"

    def getArea(self):
        return self.length * self.width


# Child class Circle
class Circle(My_shape):
    def __init__(self, color="default_color", is_filled=True, x_center=0, y_center=0, radius=1):
        super().__init__(color, is_filled)
        self.x_center = x_center
        self.y_center = y_center
        self.radius = radius

    def __str__(self):
        return f"{super().__str__()}, Type: Circle, Center: ({self.x_center}, {self.y_center}), Radius: {self.radius}"

    def getArea(self):
        return 3.14 * self.radius**2


# Console input for Rectangle creation
color_input = input("Enter color for the rectangle: ")
is_filled_input = input("Is the rectangle filled? (True/False): ").lower() == 'true'
x_top_left_input = float(input("Enter x-coordinate of top-left corner: "))
y_top_left_input = float(input("Enter y-coordinate of top-left corner: "))
length_input = float(input("Enter length of the rectangle: "))
width_input = float(input("Enter width of the rectangle: "))

# Creating Rectangle object
rectangle_obj = Rectangle(color=color_input, is_filled=is_filled_input, x_top_left=x_top_left_input,
                          y_top_left=y_top_left_input, length=length_input, width=width_input)

# Outputting rectangle details
print(rectangle_obj)
print(f"Area: {rectangle_obj.getArea()}")

