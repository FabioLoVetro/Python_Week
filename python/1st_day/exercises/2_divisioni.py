# FROM https://www.hackerrank.com/challenges/python-division/problem
# Task
# The provided code stub reads two integers,  and , from STDIN.
#
# Add logic to print two lines. The first line should contain the result of integer division,
# a//b . The second line should contain the result of float division,  a/b .
#
# No rounding or formatting is necessary.

if __name__ == '__main__':
    a = int(input("type the first number "))
    b = int(input("type the second number "))
    # python always returns a float as a result of division even if we are working with integers
    # print(int(a/b))
    print(a // b)
    print(float(a / b))
