def get_digits(num):
    digits_list = []
    if num > 999 and num <9999:
       th_dig = num/1000 
       th_res = num %1000
       hun_dig = th_res/100
       hun_res = th_res%100
       ten_dig = hun_res/10
       ten_res = hun_res%10
       digits_list =[th_dig,hun_dig,ten_dig,ten_res] 
    elif num > 99 and num <999:
       hun_dig = num/100
       hun_res = num%100
       ten_dig = hun_res/10
       ten_res = hun_res%10
       digits_list =[hun_dig,ten_dig,ten_res] 
    elif num > 9 and num <99:
       ten_dig = num/10
       ten_res = num%10
       digits_list =[ten_dig,ten_res] 
    return digits_list

def main():
    """
        https://projecteuler.net/problem=30
        This solution checks numbers till 10000
    """
    def sum_pow(m_list):
        sum =0
        for mn in m_list:
           sum = sum + mn**5
        return sum
    for n in range(9,10000):
       dig_list = get_digits(n)
       #print dig_list
       if len(dig_list)>0:
          res = sum_pow(dig_list)
          if n == res:
             print n

if __name__ == "__main__":
     main()
    
