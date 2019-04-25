def check_prime(number):
    for x in range(2,int(number/2)):
        if number%x == 0:
            return False
    return True

def check_chars(num_str):
    len_num_str= len(num_str)
    num_str_list = [str(x) for x in range(len_num_str)]
    num_list = [int(x) for x in num_str]
    num_list.sort()
    if num_list[-1] != (len(num_str)-1):
        return False
    for i in num_str:
        if i not in num_str_list:
            return False
    return True

def check_pandigital(number):
    num_str = str(number)
    if len(set(list(num_str))) == len(list(num_str)):
        if check_chars(num_str):
            return True
    return False

def main():
    """

       This is the solution for the problem 41
       https://projecteuler.net/problem=41

    """
    n=7654321
    for val in range(n, 2, -2):
        if check_pandigital(val):
            print(val)
            if check_prime(val) == True:
               print("***")
               print(val)
               break

if __name__ == "__main__":
    main()
