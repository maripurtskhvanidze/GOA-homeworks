name=input("enter your name: ")
surname=input("enter your surname: ")
age=input("enter your age: ")

print("hello my name is", name, "my surname is", surname, "my age is", age)
print("hello, my name is {}." "my surname is {}." "my age is{}.".formath(name, surname, age))


def my_split(main_string, string_to_split):
my_split=main_string.split(string_to_split)
print(my_split)
main_string=input("enter main string: ")
string_to_split=input("enter split string: ")
