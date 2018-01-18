def check_valid_combination(num):
    if len(str(num)) != 10:
       return False
    check_dict = {}
    for i in range(0,10):
      check_dict[i]=False 
    def check_num(j):
        if check_dict[int(j)] == False:
            check_dict[int(j)] = True
        else: 
           return True
        return False
    return reduce(lambda x,y:x|y,[check_num(x) for x in list(str(num))])==False

def main():
   """
      https://projecteuler.net/problem=24
   """
   #approach 1
   #valid_comb = filter(check_valid_combination, range(123456789,9876543210))
   #approach 2
   count = 1 
   num = 1234567890 
   while True:
      num = num+1
      if num > 9876543210:
          break
      if check_valid_combination(num):      
         print num," ",count
         count = count + 1
         if count == 1000000:
             print num
             break

if __name__ == '__main__':
    main()
