def greet():
    print("Hello World")
greet()


def numbers(x, y):
    numbers(7, 7)
    print(x + y)

def odd_even(numbers):
    for num in numbers:
        if num % 2 == 0:
            print(f"{num} is even")
        else:
            print(f"{num} is odd")
