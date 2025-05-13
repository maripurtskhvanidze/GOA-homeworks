def manual_list(start, end, step, user_num):
    result = [num for num in range(start, end, step) if num > user_num]
    return result

# ფუნქციის გამოძახება 3-ჯერ განსხვავებული არგუმენტებით
print(manual_list(1, 20, 2, 5))   # [7, 9, 11, 13, 15, 17, 19]
print(manual_list(10, 50, 5, 25)) # [30, 35, 40, 45]
print(manual_list(-10, 10, 3, -2)) # [1, 4, 7]
