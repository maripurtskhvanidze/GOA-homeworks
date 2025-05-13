range= range(20, 51)
range2= range(100, 151)

even_numbers= range(20, 51, 2)
odd_numbers= range(11, 31, 2)

for i in range(10):
    print("Mari Purtskhvanidze")


for i in range(10, 31):
    print(i/2)

for i in range(40, 61):
    print(i**3)


num1, num2, num3, num4, num5=int(input("enter number:")), int(input("enter number:")), int(input("enter number:")), int(input("enter number:")), int(input("enter number:"))
for i in range(5):
    print(num1, num2, num3, num4, num5)


name=input("enter your name: ")
for letter in name:
    print(letter)


num1, num2, num3=int(input("enter number: ")), int(input("enter number: ")), int(input("enter number: "))
for i in range(num1, num2, num3):
    print(i**2)


sum=0
for num in range(5, 16):
    sum += num
print(sum)