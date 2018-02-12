def left_list(num):
    ret_list = []
    length = len(str(num))
    count = 0
    while count < length :
       ret_list.append(num/(10**count)) 
       count += 1
    return ret_list

def right_list(num):
    ret_list = []
    length = len(str(num))
    while length > 0:
       ret_list.append(num%(10**length)) 
       length -= 1
    return ret_list

def check_prime(num):
    flag = True
    for i in range(2,num-1):
        if num%i == 0:
            return False
    return True 
    

def check_all_prime(p_list):
    return len(filter(check_prime,p_list)) == len(p_list)

def main():
   """
       https://projecteuler.net/problem=37
   """
   trunk_prime_list = []
   count = 10
   res_count = 0
   while True:
       r_list=right_list(count)
       l_list=left_list(count)
       #print r_list
       #print l_list
       if check_all_prime(r_list) and check_all_prime(l_list):
          trunk_prime_list.append(count)
          res_count += 1
       count +=1
       if res_count == 11:
          break
   print trunk_prime_list
   print reduce(lambda x,y: x+y, trunk_prime_list)

if __name__ == '__main__':
    main()
