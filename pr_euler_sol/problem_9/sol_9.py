def main():
    """ 
       This is the solution for the problem 9
       https://projecteuler.net/problem=9
    """ 
    for a in range(0,1000):
        for b in range(a,1000):
            for c in range(b,1000):
                if (c*c == (a*a + b*b)) and (a+b+c == 1000):
                    print a, b ,c

if __name__ == '__main__':
    main()
