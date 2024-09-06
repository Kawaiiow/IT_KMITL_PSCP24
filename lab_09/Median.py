"""Median"""
import math
def main():
    """Median"""
    n = int(input())
    x =[]
    median = ((n+1)/2) -1
    for _ in range(n):
        x.append(float(input()))
    x.sort()
    if n %2 :
        print(f"{x[int(median)]:.3f}")
    else :
        print(f"{(x[math.floor(median)]+x[math.ceil(median)])/2:.3f}")
main()
