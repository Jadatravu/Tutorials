def tria_numbers(n):
    return n*int((n+1)/2)

def penta_numbers(n):
    return n*int(((3*n)-1)/2)

def hexa_numbers(n):
    return n*((2*n)-1)

def main():
    """
       This is the solution for the problem 45
       https://projecteuler.net/problem=45
    """
    numbers_count = 100000
    tria_num_list = [tria_numbers(x) for x in range(numbers_count)]
    penta_num_list = [penta_numbers(x) for x in range(numbers_count)]
    hexa_num_list = [hexa_numbers(x) for x in range(numbers_count)]

    s1=set(tria_num_list).intersection(set(penta_num_list))
    s2=s1.intersection(hexa_num_list)
    print(s2)

if __name__=='__main__':
    main()
