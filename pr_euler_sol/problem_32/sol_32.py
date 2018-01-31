def check_func(num1,num2):
    product = num1*num2
    set_len = len((str(product))) + len((str(num1))) + len((str(num2))) 
    if set_len != 9:
       return
    else:
       res_list = list(set(str(product)) | set(str(num1)) | set(str(num2))) 
       res_list.sort()
       res_set = set(res_list)
       if len(res_set) == 9 and res_list[0] != '0':
          #print res_list
          print num1," ",num2," ",product

def main():
    """
        https://projecteuler.net/problem=32
        checks for muliplier and multipilcand in range 1 to 998
    """
    for num1 in range(1,999):
        for num2 in range(1,999):
            check_func(num1,num2)

if __name__ == '__main__':
   main()
