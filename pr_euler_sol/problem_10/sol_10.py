def is_prime(num):
    for i in range(2,num/2,1):
        if num%i ==0:
            return False
    return True  

def main():
    prime_list = filter(is_prime, range(3,200000,1))
    print reduce(lambda x,y:x+y, prime_list)

if __name__ == '__main__':
    main()
