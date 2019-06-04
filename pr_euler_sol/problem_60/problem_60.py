def check_prime(num):
    for i1 in range(2,int(num/2)):
        if num%i1 == 0:
            return False
    return True


def main():
    """
       This is the solution for the problem 60
       https://projecteuler.net/problem=60
    """
    primes = [ x for x in range(3,1000) if check_prime(x) ]
    break_flag = False
    for i1 in range(len(primes)):
        for i2 in range(i1+1, len(primes)):
            for i3 in range(i2+1, len(primes)):
                for i4 in range(i3+1, len(primes)):
                    for i5 in range(i4+1, len(primes)):
                        sum_val = primes[i1]+primes[i2]+primes[i3]+primes[i4]+primes[i5]
                        l1_list = [primes[i1],primes[i2],primes[i3],primes[i4],primes[i5]]
                        if check_prime(sum_val):
                            print(l1_list)
                            check_flag = True
                            a_break_flag = False
                            for li1 in range(len(l1_list)):
                                for li2 in range(li1+1,len(l1_list)):
                                    st1 = str(l1_list[li1])+str(l1_list[li2])
                                    st2 = str(l1_list[li2])+str(l1_list[li1])
                                    if check_prime(int(st1)) and check_prime(int(st2)):
                                        print("&&&&&&&&&&&&&&&&&&&")
                                        print(st1)
                                        print(st2)
                                        print(sum_val)
                                        print(l1_list)
                                        print("***********************")
                                        break_flag = True
                                        break
                                    else:
                                        check_flag = False
                                        a_break_flag = True
                                    if a_break_flag:
                                        break
                                if a_break_flag:
                                    break
                                if break_flag:
                                    break
                        if break_flag:
                            break
                    if break_flag:
                        break
                if break_flag:
                    break
            if break_flag:
                break
        if break_flag:
            break
        

if __name__ == "__main__":
    main()
