def apply_to_list(func, values):
    return [func(x) for x in values]

def square(x):
    return x * x

numbers = [1, 2, 3, 4, 5]
result = apply_to_list(square, numbers)
print(result)