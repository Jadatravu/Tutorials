def check_prime(num):
    for a in range(2,num-1):
          if num % a == 0:
             return False
    return True

def main():
   up_value = 600851475143 
   #up_value = 13195 
   up_check = up_value/2 
   u_list = []
   count = 2
   while count < up_check:
      if check_prime(count):
         if up_value%count == 0: 
            u_list.append(count)
            print count
      count = count+1
   print u_list
   print "largest prime factor is : %s"%str(u_list[-1])

if __name__ == '__main__':
   main()
           
