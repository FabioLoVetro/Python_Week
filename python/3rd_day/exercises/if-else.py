# FROM https://www.hackerrank.com/challenges/py-if-else/problem
# Task
# Given an integer,n , perform the following conditional actions:
#
# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater than 20, print Not Weird
# Input Format
#
# A single line containing a positive integer, n.

# !/bin/python3

if __name__ == '__main__':
    n = int(input("Type the number ").strip())

if n % 2 == 1:
    print("Weird")
elif n >= 2 and n <= 5:
    print("Not Weird")
elif n >= 6 and n <= 20:
    print("Weird")
else:
    print("Not Weird")


# we can make it a bit better

n = int(input("Type the number ").strip())

if n % 2 == 1 or (6 <= n <= 20):
    print("Weird")
else:
    print("Not Weird")
