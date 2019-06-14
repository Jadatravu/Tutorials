def get_cube_root(num):
    val = round(num**(1.0/3.0))
    if val*val*val == num:
        return True, val
    else:
        return False, val

def check_num_str(sm,num):
    sm_str = str(sm)
    num_str = str(num)
    sm_str_1 = [int(x) for x in sm_str]
    num_str_1 = [int(x) for x in num_str]
    num_str_1.sort(reverse=True)
    sm_str_1.sort(reverse=True)
    if sm_str_1 == num_str_1:
        return True
    else:
        return False

def check_all_comb(num):
    num_str = str(num)
    list_n_str = list(num_str)
    list_num_str = [int(x) for x in list_n_str]
    list_num_str.sort(reverse=True)
    sm = 0
    for i1 in list_num_str:
        sm = sm*10 + int(i1)
    list_num_str1 = list_num_str
    list_num_str1.sort(reverse=False)
    sm1 = 0
    for i2 in list_num_str1:
        sm1 = sm1*10 + int(i2)
    flag_count = 0
    l1=[]
    for a1 in range(sm1,sm):
        if check_num_str(sm,a1):
            res_flag,res_val = get_cube_root(a1)
            if res_flag:
                flag_count += 1
                l1.append(a1)
                print(l1)
    #if flag_count == 5:
    #    print(l1)
    return l1

def main():
    """
       This is the solution for the problem 62
       https://projecteuler.net/problem=62
    """
    for a1 in range(41063625,99999999):
        l1 = check_all_comb(a1)
        if len(l1) > 1:
            print(l1)

if __name__ == "__main__":
    main()
