from functools import reduce

def a_pow_b(a,b):
    l1=[]
    l1 = [a for i in range(b)]
    val = reduce(lambda x,y: x*y,l1)
    return val

def get_digit_sum(num):
    num_str = str(num)
    sum_i = int(reduce(lambda x,y: int(x)+int(y),num_str))
    return sum_i

def main():
    """
       This is the solution for the problem 56
       https://projecteuler.net/problem=56
    """
    o_sum = 0
    a1_max = b1_max = 0
    pow_val = 0
    for a1 in range(2,100):
        for b1 in range(2,100):
            pow_val = a_pow_b(a1,b1)
            val = get_digit_sum(pow_val)            
            if o_sum < val:
                o_sum = val
                a1_max = a1
                b1_max = b1
    print(pow_val)
    print(a1_max)
    print(b1_max)
    print(o_sum)

if __name__ == '__main__':
    main()
