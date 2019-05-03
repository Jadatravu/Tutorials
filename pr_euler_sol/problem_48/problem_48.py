import math
from functools import reduce

def my_pow(num):
    l1=[]
    l1 = [num for i in range(num)]
    val = reduce(lambda x,y: x*y,l1)
    return val


def get_value(num):
    sum = 0
    for i in range(1,num):
        sum += my_pow(i)
    return sum

def main():
    """
       This is the solution for the problem 48
       https://projecteuler.net/problem=48
    """
    val = get_value(1000)
    val_str = str(val)
    print(val_str[(len(val_str)-10):(len(val_str))])

main()
