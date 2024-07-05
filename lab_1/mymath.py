"""math"""
import math


def sin(x):
    """float"""
    return math.sin(math.radians(x))


def cos(x):
    """float"""
    return math.cos(math.radians(x))


def log(x, base):
    """float"""
    return math.log(x, base)


def fac(x):
    """int"""
    return math.factorial(x)


print((sin(90)+sin(60)**2)/(cos(245**2)+cos(45+135)))
print((fac(16)*fac(4))/fac(8))
print((15+25)/(math.sqrt((25-12)**2 + (12-15)**2)))
print(log(1234**4, 10))
print((log(4234, 5)+log(8191, 2)+71*log(156154, 10))/(log(777,7)-log(888,8)-log(999,9)))
