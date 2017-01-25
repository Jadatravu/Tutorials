def is_palindrome(num):
    num_str = str(num)
    len1 = len(num_str)
    flag = True
    for i in range(0,len1/2):
        if num_str[i] == num_str[-(i+1)]:
             continue
        else:
             flag = False
             break
    return flag

def main():
    """
       This is the solution for the problem 4
       https://projecteuler.net/problem=4
    """ 
    for n1 in range(999,100,-1):
        flag = True
        for n2 in range(999,100,-1):
            if is_palindrome(n1*n2):     
                print n1  
                print n2
                print n1*n2
                flag = False
                break
        if flag == False:
            break

if __name__ == '__main__':
    main()
