def divisible_check( num ):
    flag = True
    flag_list = []
    for a in range(2,20):
       if num%a == 0:
         flag_list.append(True)
       else:
         flag_list.append(False)
    for cflag in flag_list:
       flag = flag & cflag
    print flag_list
    print flag
    return flag

def main():
   """
       This is the solution for the problem 5
       https://projecteuler.net/problem=5
   """
   #count = 7*11*13*17*19*18*20*15*16
   count = 17*19*18*20*15*16
   while True:
      print count
      if divisible_check(count):
         print count
         break
      count = count + 1

if __name__ == '__main__':
    main()
      
    
