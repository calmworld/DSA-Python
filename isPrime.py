"""
Write a function, is_prime, that takes in a number as an argument.
The function should return a boolean indicating whether or not the given number is prime.

A prime number is a number that is only divisible by two distinct numbers: 1 and itself.

For example, 7 is a prime because it is only divisible by 1 and 7. 
For example, 6 is not a prime because it is divisible by 1, 2, 3, and 6.

You can assume that the input number is a positive integer.
"""


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


"""
In the context of checking if a number is prime, 
this condition is often used to determine if n has any divisors other than 1 and itself. 
If n % i == 0 is true for any i in the range from 2 to n-1, then n is not a prime number.
"""

print(is_prime(7)) # True
print(is_prime(6)) # False
print(is_prime(3)) # True
print(is_prime(2)) # True
print(is_prime(1)) # False
print(is_prime(0)) # False
print(is_prime(1111)) # False
print(is_prime(2347)) # True