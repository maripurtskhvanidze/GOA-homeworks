#ValueError
try:
    num = int(input("enter number: "))
except ValueError:
    print("it's an error, only enter number")


#IndexError
list = ["apple", "banana", "coconut"]
try:
    print(list[3])
except IndexError:
    print("IndexError: this index doesn't exist")


#TypeError
try:
    result = 7 = "10"
except TypeError:
    print("TypeError: can't make addition with str and int")