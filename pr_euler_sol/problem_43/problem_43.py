from functools import reduce

def get_num(num_str,s_i):
    val = int(num_str[s_i])*100 + int(num_str[s_i+1])*10 + int(num_str[s_i+2])
    return val

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
       This is the solution for the problem 43
       https://projecteuler.net/problem=43
    """
    num_list = []
    
    for no in range(1023456789,9876543210):
           
        if check_pandigital(no) == False:
            continue
        num_str = str(no)
        
        l7_val = get_num(num_str,(len(num_str)-3))
        
        if l7_val%17 != 0:
            continue
        
        l6_val = get_num(num_str,(len(num_str)-4))
        if l6_val%13 != 0:
            continue
        l5_val = get_num(num_str,(len(num_str)-5))
        if l5_val%11 != 0:
            continue
        l4_val = get_num(num_str,(len(num_str)-6))
        if l4_val%7 != 0:
            continue
        l3_val = get_num(num_str,(len(num_str)-7))
        if l3_val%5 != 0:
            continue
        l2_val = get_num(num_str,(len(num_str)-8))
        if l2_val%3 != 0:
            continue
        l1_val = get_num(num_str,(len(num_str)-9))
        if l1_val%2 != 0:
            continue
        print(no)
        num_list.append(no)

    total = reduce(lambda x,y:x+y, num_list)
    print(total)

if __name__ == '__main__':
    main()

