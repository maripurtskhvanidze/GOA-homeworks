try:
    a = float(input("enter the first number: "))
    b = float(input("enter the second number: "))
    print("result:", a / b)
except ZeroDivisionError:
    print("you can't divide by zero.")
except ValueError:
    print("please enter valid numbers.")


fruits = ["apple", "banana", "peach"]
try:
    index = int(input("enter an index (0-2): "))
    print("Selected:", fruits[index])
except IndexError:
    print("Index is out of range")
except ValueError:
    print("please enter number")



info = {"name": "Mari", "age": 15}
key = input("enter a key (name or age): ")
try:
    print("Value:", info[key])
except KeyError:
    print("key not found")



s = input("enter a number: ")
try:
    num = int(s)
    print("converted number: ")
except ValueError:
    print("invalid number")
