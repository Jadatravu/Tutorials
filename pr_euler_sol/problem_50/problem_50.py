def check_prime(num):
    for i1 in range(2,int(num/2)):
        if num%i1 == 0:
            return False
    return True

def main():
    """
       This is the solution for the problem 50
       https://projecteuler.net/problem=50
    """

    primes = [ x for x in range(1000000) if check_prime(x) ]
    
    sum = 0
    primes_check_list = []
    for i in range(len(primes)):
        sum += primes[i]
        if sum > primes[-1]:
            break
        if sum in primes:
            primes_check_list.append(sum)
    
    primes_check_list.sort()
    print(primes_check_list[-1])
        

if __name__ == "__main__":
    main()
