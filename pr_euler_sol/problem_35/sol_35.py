def rotate_once(num):
    num_str = list(str(num))
    l_char = num_str[0]
    for i in range(1,len(num_str)):
        loc = i - len(num_str)
        num_str[loc-1] = num_str[loc]
    num_str[-1] = l_char
    return int(''.join(num_str))

def check_prime(num):
    flag = False
    for i in range (2,num-1):
        if num%i == 0:
            flag = True
    return flag == False

def check_zero_exists(num):
    return str(num).__contains__('0')==True

def main():
    """
        https://projecteuler.net/problem=35
    """
    count = 0
    for i in range(10,1000000):
        if check_zero_exists(i):
            continue
        flag = True
        l = []
        if check_prime(i):
           new_num = rotate_once(i)
           l.append(i)
           for j in range(len(str(i))-1): 
               if check_prime(new_num):
                   l.append(new_num)
                   new_num = rotate_once(new_num) 
               else:
                   flag = False
                   break
        if flag and l:
            count += 1
            print count," ", l
    print count

if __name__ == "__main__":
    main()         
