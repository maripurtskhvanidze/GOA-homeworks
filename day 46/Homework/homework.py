squares = [x**2 for x in range(1, 6)]
print(squares)


nums = [x for x in range(1, 21) if x % 2 == 0]
print(nums)


dict = ["apple", "banana", "cherry", "date", "elderberry"]
first_letters = [dict[0] for word in dict]
print(first_letters)
