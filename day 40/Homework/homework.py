#https://www.codewars.com/kata/55f9bca8ecaa9eac7100004a/train/python
def past(h, m, s):
    return (h * 3600 + m * 60 + s) * 1000


#https://www.codewars.com/kata/57a0556c7cb1f31ab3000ad7
def repeat_str(n, s):
    return s * n



#https://www.codewars.com/kata/55f9bca8ecaa9eac7100004a
def get_sum(a, b):
    return (a + b) * (abs(a - b) + 1) / 2


#https://www.codewars.com/kata/5552101f47fc5178b1000050/train/python
def dig_pow(n, p):
    sum_of_powers, power = 0, p
    for d in str(n):
        sum_of_powers += int(d) ** power
        power += 1
    return sum_of_powers // n if sum_of_powers % n == 0 else -1
