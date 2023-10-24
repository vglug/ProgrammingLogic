import math
def is_perfect_square(a):
    if a < 0:
        return False
    square_root = math.isqrt(a)
    return square_root ** 2 == a
n=12
m=12
a=n*m
print(is_perfect_square(a)) 