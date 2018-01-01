def get_squares_sum(num):
    """
       Returns the squares sum
    """
    sum=0
    for i in range(0,num,1):
       sum=sum+i*i
    return sum

def get_sum_square(num):
    """
       Returns the sum  of squares
    """
    sum=0
    for i in range(0,num,1):
       sum = sum+i
    return sum*sum

def main():
    """
       Project Euler problem defination
       https://projecteuler.net/problem=6
    """
    #approach 1 => using custom functions
    print get_sum_square(100)-get_squares_sum(100)  
    #approach 2 => using reduce  function
    sum1= reduce(lambda x,y:x+(y*y), range(0,100))
    sum2= reduce(lambda x,y:x+y, range(0,100))
    print sum2*sum2 - sum1


if __name__ == '__main__':
   main()



