def square(N):
    for i in range(N):
        print(i*i)


square(5)





"___________________"



def even_numbers(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i


def main():
    try:
        n = int(input("Enter a number (n): "))
        if n < 0:
            
            return
        even_gen = even_numbers(n)
        
        for num in even_gen:
            print(num, end=", " if num != n and num != n - 1 else "")
        print()
    except ValueError:
        pass

if __name__ == "__main__":
    main()






def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

def main():
    try:
        n = int(input("Enter a number (n): "))
        
        
        for num in divisible_by_3_and_4(n):
            print(num, end=", " if num != n and num != n - 1 else "")
        print()
    except ValueError:
        pass

if __name__ == "__main__":
    main()



def squares(a, b):
    for num in range(a, b + 1):
        yield num ** 2


a = 1
b = 5

for square in squares(a, b):
    print(square)






def countdown(n):
    while n >= 0:
        yield n
        n -= 1


n = 5

for num in countdown(n):
    print(num)
