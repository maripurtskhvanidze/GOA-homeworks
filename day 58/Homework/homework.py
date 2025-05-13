add_five = lambda x: x + 5

multiply = lambda x, y: x * y

even = lambda x: x % 2 == 0

celsius_to_fahrenheit = lambda temps: list(map(lambda c: (c * 9/5) + 32, temps))

celsius_list = [0, 20, 30]
fahrenheit_list = celsius_to_fahrenheit(celsius_list)
print(fahrenheit_list)  # [32.0, 68.0, 86.0]

starts_with_A = lambda s: s.startswith('A')

