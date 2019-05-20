from functools import reduce 
from statistics import mean

def check_unique_strings(n_strs):
    len_of_strs = [len(n_str) for n_str in n_strs]
    r_flag = True
    for i2 in range(len(len_of_strs) -1):
        if len_of_strs[i2] != len_of_strs[i2+1]:
            r_flag = False
    if r_flag:
        for i3 in range(len(n_strs)-1):
            f1 = n_strs[i3]
            f2 = n_strs[i3+1]
            flag = True
            for i4 in range(len(f1)):
                if f2.__contains__(f1[i4]):
                    pass
                else:
                    flag = False
                    break
            if flag == False:
                return False
        return True
    else:
        return False
    
def get_num_strs(num):
    numbers = [ i1* num for i1 in range(1,7) ]
    number_strs = [ str(n1) for n1 in numbers ]
    #print (number_strs)
    num_uni_flags = [ len(n_str ) == len(set(n_str)) for n_str in number_strs ]
    uni_flag = reduce(lambda a,b: a & b, num_uni_flags)
    if uni_flag:
        print (number_strs)
        return check_unique_strings(number_strs)
    else:
        return False
  

def main():
    """
       This is the solution for the problem 52
       https://projecteuler.net/problem=52
   """
    for i in range(1,1000000):
        if get_num_strs(i) == False:
            pass
        else:
            print (i)
            break

if __name__ == "__main__":
    main()


