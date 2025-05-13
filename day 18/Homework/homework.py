num1=input("enter first number: ")
num2=input("enter second number: ")

if  num1 > num2:
    print("num1")
else:
    print(num2)



num=int(input("enter a number: "))
if num % 2 == 0:
    print("num is even number")
else:
    print("num is odd number")



correct_password="GOA BEST"
while True:
    password=input("enter password: ")

    if password == correct_password:
        print("password is correct")
    else:
        incorrect_attempts += 1
        print("imcorrect password")