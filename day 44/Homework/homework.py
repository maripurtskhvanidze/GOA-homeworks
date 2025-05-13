#https://www.codewars.com/kata/58069e4cf3c13ef3a6000168/train/python
def reverse(n):
    while n > 0:
        result = result * 10 + n % 10
        n = n / 10
    return result


#https://www.codewars.com/kata/5545f109004975ea66000086

