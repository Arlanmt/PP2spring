class StringMan:
    
    def __init__(self):
        self.input_string = ""
    """"Создается автоматически"""
    def getString(self):
        self.input_string = input("String: ")
    def printString(self):
        print(self.input_string.upper())
""""""
class Shape:
    def __init__(self):
        self.area = 0

class Square(Shape):
    def __init__(self,lenght):
        self.length = lenght
    def area(self):
        return self.length * self.length





class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width 

    def area(self):
        return self.length * self.width

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y


    def show(self):
        print(f"Coordinates of x and y here: {self.x} and {self.y}")


    def move(self, newx, newy ):
        self.newx = self.x + newx
        self.newy = self.y + newy
    def dist(self, other_point):
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5



"""BankAccount"""
class Bank():
    def __init__(self, owner,balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, deposit):
        self.balance += deposit
        print(f"New balance: {self.balance}")
    def withdraw(self, withdraw):
        if withdraw >0:
            if withdraw <= self.balance:
                self.balance -= withdraw
                print(f"New balance: {self.balance}")
            elif withdraw > self.balance:
                print("Error balance too low")


Ilya = Bank("ilua", 200)
Ilya.deposit(200)
Ilya.withdraw(400)



def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
prime_numbers = list(filter(lambda x: is_prime(x), numbers))

print("Prime Numbers:", prime_numbers)