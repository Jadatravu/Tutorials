def check_duplicates(num):
    str_num = str(num)
    return len(str_num) == len(set(str_num))

def main():
   """
       https://projecteuler.net/problem=38
   """
   count = 1
   while True:
       if check_duplicates(count) == False:
          count += 1
          continue
       st_r=''
       n_count = 1
       flag = False 
       while True:
           prod = count*n_count
           if check_duplicates(prod) == False:
               flag = True
               break
           new_set = set(list(str(st_r))).intersection(set(list(str(prod))))
           if len(new_set) > 0:
               flag = True
               break
           else:
               st_r = "{0}{1}".format(st_r,prod) 
               if len(st_r) == 9:
                   flag = True
                   if st_r.__contains__('0'):
                      pass
                   else:
                       if n_count != 1:
                          print count , "  ", st_r
                   break
               n_count +=1
       if flag:
          count += 1
       if len(str(count)) < 9:
          continue
       else:
          break

if __name__ == '__main__':
    main()
