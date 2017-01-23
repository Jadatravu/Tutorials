import math

def main():
    """
       This is the solution for the problem 16
       https://projecteuler.net/problem=16
    """
    val= pow(2, 1000)
    s_val = str(val)
    sum = 0
    for s1 in s_val:
        sum = sum + int(s1) 
    print sum

if __name__ == '__main__':
    main()
    
