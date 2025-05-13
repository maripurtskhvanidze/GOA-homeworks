list1=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for x in list1:
    print(x)


list2=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num1=int(input("enter number: "))
num2=int(input("enter number: "))

if num1>num2:
    print(list2[num2:num1])
elif num2>num1:
    print(list2[num1:num2])
else:
    print({})


list3=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list3[0])
print(list3[2])
print(list3[9])


str_list=("apple", "banana", "cherry", "melon", "watermelon")

list4=str_list[::-1]
print(list4)